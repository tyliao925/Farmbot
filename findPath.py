import torch
import cv2
import os
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.optimize import linear_sum_assignment
from ultralytics import YOLO

# Step 1: Load the YOLOv8 model
model_path='./best.pt'
model = YOLO(model_path)

# Step 2: Define a function to calculate the shortest path
def calculate_shortest_path(points):
    if len(points) <= 1:
        return points
    dist_matrix = squareform(pdist(points))
    row_ind, col_ind = linear_sum_assignment(dist_matrix)

    return points[col_ind]

# Step 3: Process each image
# Run the script on a directory of images
image_dir = '../T1'
for image_name in os.listdir(image_dir):
    if image_name.endswith('.PNG'):
        image_path = os.path.join(image_dir, image_name)
        img = cv2.imread(image_path)

        # Step 4: Get detections from YOLOv8
        results = model(img)

        centers = []
        for detection in results[0].boxes.xyxy:  # Assuming batch size of 1
            x1, y1, x2, y2 = detection

            # Calculate center of bounding box
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            centers.append([center_x.cpu(), center_y.cpu()])

        # Step 5: Calculate the shortest path between centers
        centers = np.array(centers)
        shortest_path = calculate_shortest_path(centers)

        print(f"Image: {image_name}")
        print("Shortest Path of Centers:", shortest_path)

        # Optionally, draw the shortest path on the image
        for i in range(len(shortest_path) - 1):
            start_point = tuple(map(int, shortest_path[i]))
            end_point = tuple(map(int, shortest_path[i+1]))
            img = cv2.line(img, start_point, end_point, (0, 255, 0), 2)

        # Save or display the processed image
        output_path = os.path.join(image_dir, 'processed_' + image_name)
        cv2.imwrite(output_path, img)
        # cv2.imshow('Shortest Path', img)
        # cv2.waitKey(0)



