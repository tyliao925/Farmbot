import shutil
import random
import os
import csv

IMAGE_WIDTH = 1080  # image width
IMAGE_HEIGHT = 1920  # image height

def mot_to_yolo(mot_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(mot_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            frame_id = int(row[0])
            obj_id = int(row[1])
            xmin = float(row[2])
            ymin = float(row[3])
            width = float(row[4])
            height = float(row[5])
            class_id = 0  # Assuming class is 0

            # Convert to YOLO format
            center_x = (xmin + width / 2) / IMAGE_WIDTH
            center_y = (ymin + height / 2) / IMAGE_HEIGHT
            norm_width = width / IMAGE_WIDTH
            norm_height = height / IMAGE_HEIGHT

            yolo_annotation = f"{class_id} {center_x} {center_y} {norm_width} {norm_height}\n"

            # Write YOLO annotation to a file
            yolo_file = os.path.join(output_dir, f"{frame_id:06d}.txt")
            with open(yolo_file, 'a') as out_file:
                out_file.write(yolo_annotation)

input_file = '../T1/gt/gt.txt'
output_dir = '../T1/yolo_annotations'
img_width = 1080  # Replace with actual image width
img_height = 1920  # Replace with actual image height
mot_to_yolo(input_file, output_dir)

# Paths to your dataset
dataset_dir = '../T1/'
images_dir = os.path.join(dataset_dir, 'img1')
labels_dir = os.path.join(dataset_dir, 'yolo_annotations')

# Paths for split datasets
split_dirs = {
    'train': './datasets/images/train',
    'val': './datasets/images/val',
    'test': './datasets/images/test'
}

split_label_dirs = {
    'train': './datasets/labels/train',
    'val': './datasets/labels/val',
    'test': './datasets/labels/test'
}

# Create split directories if they don't exist
for split_dir in split_dirs.values():
    if not os.path.exists(split_dir):
        os.makedirs(split_dir)

for split_label_dir in split_label_dirs.values():
    if not os.path.exists(split_label_dir):
        os.makedirs(split_label_dir)

# Get list of all images and labels
all_images = [f for f in os.listdir(images_dir) if f.endswith('.PNG')]
all_labels = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]

# Ensure image and label files match
assert len(all_images) == len(all_labels), "Number of images and labels do not match."

# Shuffle and split data
random.shuffle(all_images)
total_count = len(all_images)
train_count = int(total_count * 0.7)
val_count = int(total_count * 0.2)

train_images = all_images[:train_count]
val_images = all_images[train_count:train_count + val_count]
test_images = all_images[train_count + val_count:]


def move_files(file_list, source_images, source_labels, dest_images, dest_labels):
    for file_name in file_list:
        image_file = os.path.join(source_images, file_name)
        label_file = os.path.join(source_labels, file_name.replace('.PNG', '.txt'))

        if os.path.isfile(image_file):
            shutil.copy(image_file, dest_images)
        if os.path.isfile(label_file):
            shutil.copy(label_file, dest_labels)

move_files(train_images, images_dir, labels_dir, split_dirs['train'], split_label_dirs['train'])
move_files(val_images, images_dir, labels_dir, split_dirs['val'], split_label_dirs['val'])
move_files(test_images, images_dir, labels_dir, split_dirs['test'], split_label_dirs['test'])

print("Dataset splitting completed.")
