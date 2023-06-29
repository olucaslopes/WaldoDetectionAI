from ultralytics import YOLO
import os

# defining the home path
home_path = os.getcwd()
best_model_path = os.path.join(home_path, 'runs/detect/train/weights/best.pt')

model = YOLO(best_model_path)

