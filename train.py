from ultralytics import YOLO

model = YOLO('yolov8n.pt')  

# Train
model.train(data='Light-HaGRID/data.yaml', epochs=100, batch=64, imgsz=640, device=[2], save=True, name='gesture_recognition')

# nohup python -u train.py > train.log 2>&1 &