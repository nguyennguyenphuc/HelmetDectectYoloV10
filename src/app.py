import streamlit as st
from src.model import load_model
from src.predict import predict_image
from PIL import Image

path_model = 'models/yolov10n.pt'

st.title("Helmet Detection with YOLOv10")

model = load_model(path_model)

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_path = f"images/{uploaded_file.name}"
    image.save(img_path)

    predict_image(model, img_path)

    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Detecting helmets...")

    predicted_image = Image.open(f"{img_path.split('.')[0]}_predict.png")
    st.image(predicted_image, caption='Predicted Image', use_column_width=True)
