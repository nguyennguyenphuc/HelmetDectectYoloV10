# HelmetDectectYoloV10

This project uses YOLOv10 to detect workers wearing helmets in construction sites.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd my_yolov10_project
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Download and Extract Dataset
```python
from src.data_loader import download_and_extract_dataset

download_and_extract_dataset(
    'https://drive.google.com/file/d/1twdtZEfcw4ghSZIiPDypJurZnNXzMO7R/view?usp=sharing', 
    './data/safety_helmet_dataset'
)
### Train model 
```python
from src.train import train_model

train_model(
    data_path='./data/safety_helmet_dataset/data.yaml',
    model_path='./models/yolov10n.pt',
    epochs=50,
    batch_size=256,
    img_size=640
)
```
### Predict Image

```python 
from src.model import load_model
from src.predict import predict_image

model = load_model(path_model) ### path_model is path to model 
predict_image(model, './images/sample_image.jpg')

```

### Train model with helmet dataset

edit settings.yaml to change the path to the dataset from \HelmetDectectYoloV10\dataset to \HelmetDectectYoloV10

```python
python -m src.train
```

### Streamlit App

Run the Streamlit app to upload and predict images:
edit path_model in src/app.py to the path to the model

```python
streamlit run src/app.py
```