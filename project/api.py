import tempfile
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from detection import detect_image
import base64
import cv2

app = FastAPI(title="Shelf Detection API")


@app.post("/detect")
async def detect_endpoint(file: UploadFile = File(...), model_path: str = "yolov8n.pt", conf: float = 0.25):
    contents = await file.read()
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    tmp.write(contents)
    tmp.flush()
    tmp.close()
    try:
        res = detect_image(tmp.name, model_path=model_path, conf=conf)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

    annotated = res.get("annotated")
    img_b64 = None
    if isinstance(annotated, (bytes, bytearray)):
        img_b64 = base64.b64encode(annotated).decode("utf-8")
    else:
        try:
            # convert BGR numpy to JPEG
            _, jpeg = cv2.imencode('.jpg', annotated)
            img_b64 = base64.b64encode(jpeg.tobytes()).decode('utf-8')
        except Exception:
            img_b64 = None

    return {
        "count": res.get("count", 0),
        "boxes": res.get("boxes", []),
        "annotated_base64": img_b64,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
