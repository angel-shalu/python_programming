import sys
import os
from pathlib import Path

sys.path.append(os.path.dirname(__file__))

import streamlit as st
import tempfile
import cv2
import numpy as np

from detection import detect_image
from data_store import append_stock, load_stock
from predict import predict_stock
from rag import RAGAssistant


st.set_page_config(page_title="Smart Retail Shelf AI", layout="wide")

st.title("Smart Retail Shelf Monitoring — AI Assistant")

col1, col2 = st.columns([2, 1])

with col1:
	st.header("Image -> Detection")
	use_camera = st.checkbox("Use camera input (webcam)")
	uploaded = None
	if use_camera:
		cam_file = st.camera_input("Take a shelf photo")
		if cam_file is not None:
			uploaded = cam_file
	else:
		uploaded = st.file_uploader("Upload shelf image", type=["jpg", "jpeg", "png"])

	model_path = st.text_input("YOLO model path", value="yolov8n.pt")
	conf = st.slider("Confidence threshold", 0.0, 1.0, 0.25)

	if st.button("Detect & Save"):
		if uploaded is None:
			st.error("Provide an image first (upload or camera)")
		else:
			tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
			tmp.write(uploaded.getbuffer())
			tmp.flush()
			tmp.close()

			try:
				res = detect_image(tmp.name, model_path=model_path, conf=conf)
			except Exception as e:
				st.error(f"Detection failed: {e}")
				raise

			annotated = res.get("annotated")
			count = res.get("count", 0)

			# annotated is BGR -> convert to RGB
			if isinstance(annotated, np.ndarray):
				annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
				st.image(annotated_rgb, use_column_width=True)
			else:
				st.write("No annotated image available")

			st.metric("Detected products", count)
			append_stock(count)
			st.success("Saved current stock to CSV")

	if uploaded is not None and st.button("Preview detection (no save)"):
		tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
		tmp.write(uploaded.getbuffer())
		tmp.flush()
		tmp.close()
		try:
			res = detect_image(tmp.name, model_path=model_path, conf=conf)
			annotated = res.get("annotated")
			if isinstance(annotated, np.ndarray):
				annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
				st.image(annotated_rgb, use_column_width=True)
				st.metric("Detected products", res.get("count", 0))
		except Exception as e:
			st.error(f"Preview failed: {e}")

with col2:
	st.header("Analytics & Chatbot")
	df = load_stock()
	st.subheader("Recent stock log")
	if df.empty:
		st.write("No stock log found yet. Use Detect & Save to create data.")
	else:
		st.dataframe(df.tail(20))

	st.subheader("Prediction")
	days = st.number_input("Days ahead", min_value=1, max_value=365, value=7)
	if st.button("Predict"):
		pred, info = predict_stock(days_ahead=days)
		if pred is None:
			st.warning(f"Prediction unavailable: {info}")
		else:
			st.metric(f"Predicted stock in {days} days", int(pred))

	st.subheader("RAG Chatbot")
	rag = RAGAssistant()
	# build from stock CSV as simple text store
	texts = []
	for _, r in df.iterrows():
		texts.append(f"On {r['date']} stock was {int(r['stock'])}")
	if texts:
		rag.build(texts)

	q = st.text_input("Ask about stock or reports")
	if st.button("Ask") and q:
		ans = rag.answer(q)
		st.write(ans)

	st.markdown("---")
	st.markdown("**Notes:** Set `OPENAI_API_KEY` to enable LLM answers. Place `yolov8n.pt` in the workspace or change model path.")

