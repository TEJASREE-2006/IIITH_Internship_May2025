# segment_images.py

from ultralytics import YOLO
import os
import cv2

# Define input and output folders
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "segmented_images"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load the YOLOv8 segmentation model (you can also try yolov8n-seg or yolov8m-seg)
model = YOLO("yolov8s-seg.pt")  # Automatically downloads the model if not present

# List all image files in the input folder
image_files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Process each image
for image_name in image_files:
    image_path = os.path.join(INPUT_FOLDER, image_name)
    
    # Run segmentation
    results = model(image_path)

    # Save result to output folder
    for i, r in enumerate(results):
        output_path = os.path.join(OUTPUT_FOLDER, f"{os.path.splitext(image_name)[0]}_segmented.jpg")
        r.save(filename=output_path)
        print(f"Saved segmented image: {output_path}")

print("✅ Segmentation complete for all images.")
