from src.model import load_model


def predict_image(model, img_path):
    """Predict bounding boxes for an image using the given model."""
    result = model(source=img_path)[0]
    result.save(f"{img_path.split('.')[0]}_predict.png")


if __name__ == '__main__':
    model = load_model('./models/yolov10n.pt')
    predict_image(model, './images/sample_image.jpg')
