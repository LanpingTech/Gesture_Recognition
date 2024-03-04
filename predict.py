from ultralytics import YOLO


model = YOLO('runs/detect/gesture_recognition/weights/best.pt')

result = model('Light-HaGRID/images/val/395.jpg', device=[0])
result[0].save('result.jpg')

