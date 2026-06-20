import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

# ==========================
# LOAD DATASET
# ==========================
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize
x_train = x_train / 255.0
x_test = x_test / 255.0

# ==========================
# BUILD MODEL
# ==========================
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("\nTraining Model...\n")

# ==========================
# TRAIN MODEL
# ==========================
model.fit(
    x_train,
    y_train,
    epochs=5,
    verbose=1
)

# ==========================
# EVALUATE MODEL
# ==========================
loss, accuracy = model.evaluate(
    x_test,
    y_test,
    verbose=0
)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# ==========================
# SHOW MNIST PREDICTIONS
# ==========================
predictions = model.predict(
    x_test[:9],
    verbose=0
)

plt.figure(figsize=(12, 10))

plt.suptitle(
    f"Handwritten Digit Recognition\nAccuracy: {accuracy*100:.2f}%",
    fontsize=16,
    fontweight='bold'
)

for i in range(9):

    plt.subplot(3, 3, i + 1)

    plt.imshow(
        x_test[i],
        cmap='gray'
    )

    predicted = np.argmax(predictions[i])
    actual = y_test[i]
    confidence = np.max(predictions[i]) * 100

    status = "✓ Correct" if predicted == actual else "✗ Wrong"

    plt.title(
        f"Actual: {actual}\n"
        f"Predicted: {predicted}\n"
        f"Confidence: {confidence:.2f}%\n"
        f"{status}",
        fontsize=8
    )

    plt.axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

# ==========================
# CUSTOM IMAGE PREDICTION
# ==========================

image_path = input("Enter image name: ")

if os.path.exists(image_path):

    print("\nCustom Image Found!")

    img = Image.open(image_path).convert("L")

    img = img.resize((28, 28), Image.Resampling.LANCZOS)

    img_array = np.array(img)

    # MNIST format
    img_array = 255 - img_array

    img_array = img_array / 255.0

    model_input = img_array.reshape(1, 28, 28)

    prediction = model.predict(
        model_input,
        verbose=0
    )

    predicted_digit = np.argmax(prediction)

    confidence = np.max(prediction) * 100

    plt.figure(figsize=(5, 5))

    plt.imshow(
        img_array,
        cmap='gray'
    )

    plt.title(
        f"Predicted Digit: {predicted_digit}\n"
        f"Confidence: {confidence:.2f}%"
    )

    plt.axis('off')
    plt.show()

    print(f"Predicted Digit : {predicted_digit}")
    print(f"Confidence      : {confidence:.2f}%")

else:

    print(
        "\nNo custom image found.\n"
        "Place a file named 'my_digit.png' "
        "in the project folder to test your own handwriting."
    )