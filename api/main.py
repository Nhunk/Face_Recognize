import sys
import os
import cv2
import numpy as np
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import io
from PIL import Image

# Add project root to python path to import model modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.Dino import DinoFaceRecognition
from model.FaceDetection import FaceDetection

app = FastAPI(title="Face Recognition API", description="API for Automated Attendance Management", version="1.0.0")

# Initialize models
try:
    dino_model = DinoFaceRecognition()
    # Replace these paths if they are different in your actual setup
    faiss_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model', 'faiss_index.faiss')
    metadata_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model', 'faiss_index_metadata.pkl')
    
    if os.path.exists(faiss_path) and os.path.exists(metadata_path):
        dino_model.load_data(faiss_index_path=faiss_path, metadata_path=metadata_path)
    
    # We load YOLOv8 model for face detection
    yolo_model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model', 'yolov8n-face.pt')
    if not os.path.exists(yolo_model_path):
        print(f"[WARN] YOLO model not found at {yolo_model_path}")
        face_detector = None
    else:
        face_detector = FaceDetection(model_path=yolo_model_path)
except Exception as e:
    print(f"Error initializing models: {e}")

@app.get("/")
def read_root():
    return {"message": "Welcome to Face Recognition API. Use /docs to test endpoints."}

@app.post("/detect")
async def detect_faces(file: UploadFile = File(...)):
    """
    Detects faces in an image using YOLOv8. Returns bounding boxes.
    """
    if not face_detector:
        raise HTTPException(status_code=500, detail="Face detector not initialized")
    
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        boxes = face_detector.detectFaceBoxes(img)
        return {"boxes": boxes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/recognize")
async def recognize_face(file: UploadFile = File(...), threshold: int = 3200):
    """
    Recognizes a cropped face using Dinov2 + FAISS.
    """
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        result = dino_model.recognize_face_topk(img, threshold=threshold, top_k=1)
        
        if result and len(result) > 0:
            label, score = result[0]
            return {"label": label, "score": float(score)}
        else:
            return {"label": "Unknown", "score": 0.0}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
