from ultralytics import YOLO
import os

# Load the segmentation model
model = YOLO("yolov8s-seg.pt")

# Set input and output folders
input_folder = "video_frames"
output_folder = "segmented_video_frames"
os.makedirs(output_folder, exist_ok=True)

# Loop through video frames and segment them
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.png')):
        image_path = os.path.join(input_folder, filename)
        results = model(image_path)
        results[0].save(filename=os.path.join(output_folder, filename))
