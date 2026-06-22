import streamlit as st
import numpy as np
from PIL import Image
from predict import predict_array

st.set_page_config(
    page_title="Handwritten Digit Recognition",
    page_icon="✍️",
    layout="centered"
)

st.title("Handwritten Digit Recognition using CNN")

st.write(
    "Upload a handwritten digit image (0-9) and get predictions from the trained CNN model."
)

uploaded_file = st.file_uploader(
    "Upload PNG/JPG Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("L")

    st.image(
        image,
        caption="Uploaded Image",
        width=250
    )

    digit, confidence = predict_array(image)

    if digit == "INVALID":

        st.error(
            "Invalid Input. Please upload a clear handwritten digit."
        )

    elif confidence < 85:

        st.warning(
            f"Low Confidence Prediction\n\nDigit: {digit}\nConfidence: {confidence:.2f}%"
        )

    else:

        st.success(
            f"Predicted Digit: {digit}"
        )

        st.info(
            f"Confidence: {confidence:.2f}%"
        )