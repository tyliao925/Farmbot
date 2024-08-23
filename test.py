from ultralytics import YOLO

# Define paths
model_path = './best.pt'
test_images_dir = 'datasets/images/test'
ground_truth_labels_dir = 'datasets/labels/test'
output_dir = './predictions'

# Load the trained model
model = YOLO(model_path)

# Perform inference on the test dataset
if __name__ == '__main__':
    results = model.val(data='./data.yaml', imgsz=1080, batch=8, conf=0.25, iou=0.6)

