# Smart Retail Shelf Monitoring — Minimal Starter

This project demonstrates a minimal end-to-end setup combining:
- YOLOv8 detection (Ultralytics)
- Simple stock logging (CSV)
- Linear regression stock prediction (scikit-learn)
- RAG-style retrieval using SentenceTransformers + FAISS, optionally answered by OpenAI
- Streamlit dashboard to run detection, save data, predict and ask questions

Run (create virtualenv first):

```bash
pip install -r requirements.txt
streamlit run project/app.py
```

Notes:
- Provide an `OPENAI_API_KEY` in the environment if you want LLM-generated answers for the chatbot.
- Place `yolov8n.pt` model in the workspace or change the model path in the UI.
