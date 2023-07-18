import numpy as np
import cv2
import os
from ultralytics import YOLO

MODEL_PATH = 'model/model_VNPD.pt'

# Load the model
def load_model():
    model = YOLO(MODEL_PATH)
    return model

def load_image(file_path):
    return file_path

def predict(images):
    
    model = load_model()
    
    results = model.predict(source=images, save=True, save_crop=True, project="output", name="yolov8_results" )
    
    if len(results[0].boxes) == 0:
        return "No Detections were Made in this image"
    else:
        boxes = results[0].boxes
        box = boxes[0]  # returns one box
        cls_box = boxes.cpu().xywhn  # box with xywh format, (N, 4)
        cls_box = np.array(cls_box)
        return "Object(s) Detected, Results Saved in the *Output* folder"
    # return img

# print(load_image("C:\\Users\\pc\\Downloads\\istockphoto-1375640774-2048x2048.jpg"))