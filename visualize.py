import glob
import random
import cv2
import matplotlib.pyplot as plt
import os
import numpy as np

# Define paths
images_path = "dataset/train/images/*"
labels_path = "dataset/train/labels/*.txt"

# Get all image files
image_files = glob.glob(images_path)

# Randomly select 4 images
selected_images = random.sample(image_files, 4)

# Class names and colors
classes = [
    "A1", "A2", "A3", "B4", "B5", "C6", "C7", "C8", "C9", "C10",
    "C11", "C12", "D13", "D14", "D15", "E16", "E17", "E18", "F19",
    "F20", "G21", "G22", "X", "Y"
]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

def plot_bounding_boxes(image_path, label_path):
    # Load the image
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Get image dimensions
    height, width, _ = img.shape

    # Load the corresponding label file
    with open(label_path, 'r') as file:
        for line in file:
            # Parse YOLOv5 format
            class_id, x_center, y_center, bbox_width, bbox_height = map(float, line.split())
            class_id = int(class_id)  # Convert class_id to int
            
            # Convert normalized positions to pixel positions
            x_center, y_center, bbox_width, bbox_height = (x_center * width, y_center * height,
                                                           bbox_width * width, bbox_height * height)
            
            # Calculate the bounding box's top-left corner position
            x_min = int(x_center - (bbox_width / 2))
            y_min = int(y_center - (bbox_height / 2))
            
            # Get color and class name for this class_id
            color = colors[class_id]
            class_name = classes[class_id]
            
            # Draw the bounding box on the image
            cv2.rectangle(img, (x_min, y_min), (x_min + int(bbox_width), y_min + int(bbox_height)), color, 2)
            
            # Put the class name above the bounding box
            cv2.putText(img, class_name, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    # Display the image
    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.show()

plot_bounding_boxes('dataset/test/images/1050791.jpg', 'dataset/test/labels/1050791.txt')

# for image_path in selected_images:
#     # Construct the corresponding label path
#     label_filename = os.path.basename(image_path).replace('.jpg', '.txt').replace('.png', '.txt')
#     label_path = os.path.join("dataset/train/labels", label_filename)
    
#     # Plot bounding boxes on the image
#     plot_bounding_boxes(image_path, label_path)
