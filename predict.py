import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

model = load_model("digit_model.keras")


def predict_digit(image_path):

    img = Image.open(image_path).convert("L")

    img = img.resize((28, 28), Image.Resampling.LANCZOS)

    img_array = np.array(img)

    img_array = 255 - img_array

    img_array = img_array / 255.0

    model_input = img_array.reshape(1, 28, 28, 1)

    prediction = model.predict(
        model_input,
        verbose=0
    )

    predicted_digit = np.argmax(prediction)

    confidence = np.max(prediction) * 100

    return predicted_digit, confidence


def predict_array(img):

    img = img.resize((28, 28))

    pixel_array = np.array(img)

    dark_pixels = np.sum(pixel_array < 200)

    if dark_pixels > 180:
        return "INVALID", 0

    img_array = 255 - pixel_array

    img_array = img_array / 255.0

    model_input = img_array.reshape(1, 28, 28, 1)

    prediction = model.predict(
        model_input,
        verbose=0
    )

    predicted_digit = np.argmax(prediction)

    confidence = np.max(prediction) * 100

    return predicted_digit, confidence