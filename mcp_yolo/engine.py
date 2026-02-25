from ultralytics import YOLOE
import torch
import numpy as np
from PIL import Image

class YOLOEWrapper:
    """
    Wrapper for Ultralytics YOLOE model with zero-shot capabilities.
    """
    def __init__(self, model_path="yoloe-26l-seg.pt"):
        print(f"Loading YOLOE model: {model_path}")
        self.model = YOLOE(model_path)
        # Move to GPU if available
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        if torch.backends.mps.is_available():
            self.device = "mps"
        
        print(f"Using device: {self.device}")

    def detect(self, image_path: str, classes: list[str] = None):
        """
        Perform zero-shot object detection.
        """
        if classes:
            self.model.set_classes(classes)
        
        results = self.model.predict(source=image_path, device=self.device)
        
        detections = []
        for result in results:
            boxes = result.boxes
            for i in range(len(boxes)):
                box = boxes[i]
                detections.append({
                    "label": result.names[int(box.cls[0].item())],
                    "confidence": float(box.conf[0].item()),
                    "bbox": box.xyxy[0].tolist(),  # [xmin, ymin, xmax, ymax]
                })
        
        return detections

    def segment(self, image_path: str, classes: list[str] = None):
        """
        Perform zero-shot instance segmentation.
        """
        if classes:
            self.model.set_classes(classes)
            
        results = self.model.predict(source=image_path, device=self.device)
        
        segmentations = []
        for result in results:
            if result.masks is not None:
                for i in range(len(result.masks)):
                    mask = result.masks[i]
                    # Get polygon coordinates
                    polygon = mask.xy[0].tolist() 
                    segmentations.append({
                        "label": result.names[int(result.boxes[i].cls[0].item())],
                        "confidence": float(result.boxes[i].conf[0].item()),
                        "bbox": result.boxes[i].xyxy[0].tolist(),
                        "polygon": polygon
                    })
        
        return segmentations
