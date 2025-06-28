# Task 4 - Snack Detection using YOLOv5

This project trains a YOLOv5 model to detect snacks using a custom dataset.

## Steps

- Model: yolov5s
- Image Size: 640
- Epochs: 50
- Batch: 16

## Results

Trained weights: [Download best.pt](https://drive.google.com/your-link)

## To Run Validation:
```bash
python val.py --data data.yaml --weights best.pt --img 640
