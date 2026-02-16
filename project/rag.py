import os
import requests
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

try:
    from openai import OpenAI
except Exception:
    OpenAI = None


class RAGAssistant:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.embed_model = SentenceTransformer(model_name)
        self.index = None
        self.texts = []

    def build(self, texts):
        self.texts = texts.copy()
        embs = self.embed_model.encode(self.texts, convert_to_numpy=True)
        d = embs.shape[1]
        self.index = faiss.IndexFlatL2(d)
        self.index.add(embs.astype('float32'))

    def add(self, text):
        self.texts.append(text)
        emb = self.embed_model.encode([text], convert_to_numpy=True).astype('float32')
        if self.index is None:
            d = emb.shape[1]
            self.index = faiss.IndexFlatL2(d)
        self.index.add(emb)

    def retrieve(self, query, k=3):
        if self.index is None:
            return []
        q_emb = self.embed_model.encode([query], convert_to_numpy=True).astype('float32')
        D, I = self.index.search(q_emb, k)
        docs = [self.texts[i] for i in I[0] if i != -1]
        return docs

    def _hf_inference(self, prompt, model="google/flan-t5-small", token=None, max_tokens=256):
        if token is None:
            return None
        url = f"https://api-inference.huggingface.co/models/{model}"
        headers = {"Authorization": f"Bearer {token}"}
        payload = {"inputs": prompt, "parameters": {"max_new_tokens": max_tokens}}
        try:
            r = requests.post(url, headers=headers, json=payload, timeout=30)
            if r.ok:
                data = r.json()
                if isinstance(data, list) and "generated_text" in data[0]:
                    return data[0]["generated_text"]
                if isinstance(data, dict) and "generated_text" in data:
                    return data["generated_text"]
                if isinstance(data, str):
                    return data
        except Exception:
            pass
        return None

    def answer(self, query, k=3, openai_model="gpt-3.5-turbo"):
        docs = self.retrieve(query, k)
        ctx = "\n\n".join(docs)
        prompt = f"Use the context to answer the question. If unknown, say you don't know.\n\nContext:\n{ctx}\n\nQuestion: {query}"

        # 1) OpenAI (preferred if key configured)
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if openai_api_key and OpenAI is not None:
            try:
                client = OpenAI(api_key=openai_api_key)
                resp = client.chat.completions.create(model=openai_model, messages=[{"role": "user", "content": prompt}], max_tokens=256)
                return resp.choices[0].message.content.strip()
            except Exception:
                pass

        # 2) Hugging Face Inference API fallback
        hf_token = os.getenv("HUGGINGFACE_API_TOKEN")
        hf_model = os.getenv("HUGGINGFACE_MODEL", "google/flan-t5-small")
        if hf_token:
            out = self._hf_inference(prompt, model=hf_model, token=hf_token)
            if out:
                return out

        # 3) Local transformers pipeline fallback (no key)
        local_model = os.getenv("LOCAL_LLM_MODEL")
        if local_model:
            try:
                from transformers import pipeline
                pipe = pipeline("text2text-generation", model=local_model)
                res = pipe(prompt, max_length=256)
                if isinstance(res, list) and len(res) > 0 and "generated_text" in res[0]:
                    return res[0]["generated_text"]
                if isinstance(res, list) and len(res) > 0 and "text" in res[0]:
                    return res[0]["text"]
            except Exception:
                pass

        # final fallback: return retrieved docs or message
        if ctx:
            return ctx
        return "No context available. Set OPENAI_API_KEY or HUGGINGFACE_API_TOKEN, or configure LOCAL_LLM_MODEL."

    def save(self, path_prefix: str):
        """Save FAISS index and texts to disk using given path prefix (without extension)."""
        if self.index is None:
            raise ValueError("No index to save")
        dirpath = os.path.dirname(path_prefix)
        if dirpath and not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)
        # write faiss index
        faiss.write_index(self.index, f"{path_prefix}.index")
        # save texts
        np.save(f"{path_prefix}_texts.npy", np.array(self.texts, dtype=object), allow_pickle=True)

    def load(self, path_prefix: str):
        """Load FAISS index and texts from disk using given path prefix (without extension)."""
        idx_file = f"{path_prefix}.index"
        texts_file = f"{path_prefix}_texts.npy"
        if not os.path.exists(idx_file) or not os.path.exists(texts_file):
            raise FileNotFoundError("Index or texts file not found")
        self.index = faiss.read_index(idx_file)
        arr = np.load(texts_file, allow_pickle=True)
        self.texts = arr.tolist()
