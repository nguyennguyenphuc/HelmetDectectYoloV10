from ultralytics import YOLO
from src.data_loader import download_and_extract_dataset
import requests


def download_file(url, model_path):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    with open(model_path, 'wb') as file:
        file.write(response.content)
    print(f"File downloaded successfully: {model_path}")


def train_model(data_path, model_path, epochs=1, batch_size=32, img_size=640):
    """Train YOLOv10 model on the given dataset."""
    model = YOLO(model_path)
    model.train(
        data=data_path,
        epochs=epochs,
        batch=batch_size,
        imgsz=img_size
    )


# Example usage
# train_model('./data/safety_helmet_dataset/data.yaml', './models/yolov10n.pt', 50, 256, 640)
if __name__ == '__main__':

    url = "https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt"
    model_path = "./models/yolov10n.pt"
    download_file(url, model_path)

    download_and_extract_dataset(
        '1twdtZEfcw4ghSZIiPDypJurZnNXzMO7R',
        './data/safety_helmet_dataset'
    )

    train_model('./data/safety_helmet_dataset/data.yaml',
                './models/yolov10n.pt')
