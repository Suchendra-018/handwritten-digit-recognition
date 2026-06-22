import tkinter as tk
from predict import predict_array
from PIL import Image, ImageDraw

root = tk.Tk()

root.title(" Handwritten Digit Recognition")
root.geometry("600x700")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Handwritten Digit Recognition",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)

canvas = tk.Canvas(
    root,
    width=350,
    height=350,
    bg="white",
    cursor="cross"
)
canvas.pack(pady=20)

image = Image.new("L", (300, 300), "white")
draw_image = ImageDraw.Draw(image)


def draw(event):

    x = event.x
    y = event.y

    canvas.create_oval(
        x - 8,
        y - 8,
        x + 8,
        y + 8,
        fill="black",
        outline="black"
    )

    draw_image.ellipse(
        [x - 8, y - 8, x + 8, y + 8],
        fill="black"
    )

canvas.bind("<B1-Motion>", draw)

result_label = tk.Label(
    root,
    text="Draw a digit and click Predict",
    font=("Arial", 16,"bold")
)
result_label.pack(pady=10)

def clear_canvas():

    global image, draw_image

    canvas.delete("all")

    image = Image.new("L", (300, 300), "white")
    draw_image = ImageDraw.Draw(image)

    result_label.config(
        text="Draw a digit and click Predict"
    )

def predict_canvas():

    digit, confidence = predict_array(image)
    if digit == "INVALID":

        result_label.config(
            text=(
                "Invalid Input\n"
                "Please draw a single digit (0-9)"
            )
        )
    elif confidence < 85:

        result_label.config(
            text=(
            f"Predicted: {digit}\n"
            f"Confidence: {confidence:.2f}%\n"
            f"Low confidence - try drawing more clearly"
        )
        )

    else:

        result_label.config(
            text=(
                f"Prediction: {digit}\n"
                f"Confidence: {confidence:.2f}%"
            )
        )

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

predict_button = tk.Button(
    button_frame,
    text="Predict",
    width=15,
    height=2,
    command=predict_canvas
)
predict_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    width=15,
    height=2,
    command=clear_canvas
)
clear_button.grid(row=0, column=1, padx=10)

root.mainloop()