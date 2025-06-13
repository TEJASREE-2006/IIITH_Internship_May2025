from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # Light, fast model
model.train(data='https://raw.githubusercontent.com/ultralytics/ultralytics/main/ultralytics/cfg/datasets/african-wildlife.yaml', epochs=13, imgsz=640)
