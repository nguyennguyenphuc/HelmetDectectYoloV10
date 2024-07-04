from ultralytics import YOLO

def load_model(model_path):
    """Load YOLOv10 model from the given path."""
    return YOLO(model_path)

