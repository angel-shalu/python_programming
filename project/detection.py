from ultralytics import YOLO
import cv2
import torch


def detect_image(image_path, model_path="yolov8n.pt", conf=0.25):
    """Run YOLOv8 on an image and return count, boxes and annotated image.

    Returns: dict with keys: count, boxes (list), annotated (BGR numpy image)
    """
    # Determine device (GPU if available, else CPU)
    device = 0 if torch.cuda.is_available() else 'cpu'
    model = YOLO(model_path)
    model = model.to(device)
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    results = model(img, conf=conf, verbose=False)
    res = results[0]

    boxes = []
    if hasattr(res, "boxes") and len(res.boxes) > 0:
        xyxy = res.boxes.xyxy.cpu().numpy()
        cls = res.boxes.cls.cpu().numpy()
        confs = res.boxes.conf.cpu().numpy()
        for b, c, cf in zip(xyxy, cls, confs):
            boxes.append({"xyxy": b.tolist(), "class": int(c), "conf": float(cf)})

    # annotated image (BGR)
    try:
        annotated = res.plot()  # numpy array BGR
    except Exception:
        annotated = img

    return {"count": len(boxes), "boxes": boxes, "annotated": annotated}
