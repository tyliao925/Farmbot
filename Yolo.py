from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('./yolov8n.yaml')
    model.train(data='./data.yaml', epochs=5, imgsz=1920, batch=2)
