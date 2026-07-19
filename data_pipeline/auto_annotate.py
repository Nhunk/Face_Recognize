import os
import cv2
from ultralytics import YOLO
import sys

# Define root to access models
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

def auto_annotate(video_path, person_name, output_base="train_img", skip_frames=5):
    """
    Extract faces from a video and save them to a designated folder for a person.
    This acts as an automatic data annotation pipeline.
    """
    # Load YOLOv8 face model
    model_path = os.path.join(root_dir, 'model', 'yolov8n-face.pt')
    if not os.path.exists(model_path):
        print(f"Error: YOLO model not found at {model_path}")
        return

    model = YOLO(model_path)
    
    # Create output directory for the person
    output_dir = os.path.join(root_dir, output_base, person_name)
    os.makedirs(output_dir, exist_ok=True)
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return
        
    frame_count = 0
    saved_count = 0
    
    print(f"Starting auto-annotation for '{person_name}'...")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Process every nth frame to avoid nearly identical images
        if frame_count % skip_frames == 0:
            results = model(frame, verbose=False)
            
            for result in results:
                for box in result.boxes:
                    # Bounding box coordinates
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    
                    # Optional: Add padding
                    padding = 20
                    h, w, _ = frame.shape
                    x1 = max(0, x1 - padding)
                    y1 = max(0, y1 - padding)
                    x2 = min(w, x2 + padding)
                    y2 = min(h, y2 + padding)
                    
                    # Crop face
                    face_crop = frame[y1:y2, x1:x2]
                    
                    if face_crop.size > 0:
                        face_crop = cv2.resize(face_crop, (256, 256))
                        save_path = os.path.join(output_dir, f"{person_name}_{saved_count}.jpg")
                        cv2.imwrite(save_path, face_crop)
                        saved_count += 1
                        
        frame_count += 1
        
    cap.release()
    print(f"Finished auto-annotation. Saved {saved_count} face images to {output_dir}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Auto Annotate Faces from Video")
    parser.add_argument("--video", type=str, required=True, help="Path to input video")
    parser.add_argument("--name", type=str, required=True, help="Name of the person (label)")
    parser.add_argument("--out", type=str, default="train_img", help="Output base directory")
    
    args = parser.parse_args()
    auto_annotate(args.video, args.name, args.out)
