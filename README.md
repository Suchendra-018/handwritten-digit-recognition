# Handwritten Digit Recognition using MNIST Dataset

## Project Overview

This project is an AI application that recognizes handwritten digits from images using a Neural Network trained on the MNIST dataset.

The model is trained on 60,000 handwritten digit images and tested on 10,000 images. After training, the application can predict digits from both the MNIST dataset and user-provided handwritten images.

---

## Features

* Train a Neural Network using the MNIST dataset
* Achieve approximately 97%–99% accuracy
* Predict handwritten digits from images
* Display actual and predicted digits
* Show confidence score
* Display prediction status
* Visualize handwritten digit images

---

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Matplotlib
* Pillow (PIL)

---

## Python Version

Recommended:

Python 3.13

Check version:

```bash
python --version
```

---

## Project Structure

```text
handwritten-digit-recognition/
│
├── main.py
├── my_digit.png
└── README.md
```

---

## Create Virtual Environment

Open PowerShell inside the project folder.

Create virtual environment:

```powershell
py -3.13 -m venv .venv
```

Activate virtual environment:

```powershell
.\.venv\Scripts\activate
```

After activation:

```text
(.venv) PS C:\path\to\project>
```

---

## Install Required Libraries

Install all dependencies:

```powershell
pip install numpy matplotlib tensorflow pillow
```

Verify installation:

```powershell
python -c "import numpy, matplotlib, tensorflow, PIL; print('Libraries Installed Successfully')"
```

---

## Running the Project

Execute:

```powershell
python main.py
```

The application will:

1. Load the MNIST dataset
2. Train the Neural Network
3. Evaluate model accuracy
4. Display sample digit predictions
5. Predict user-provided handwritten images

---

## MNIST Dataset Information

Training Images: 60,000

Testing Images: 10,000

Image Size:

```text
28 × 28 pixels
```

Classes:

```text
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

---

## Testing with Your Own Handwritten Image

### Step 1: Open Paint

Press:

```text
Windows + R
```

Type:

```text
mspaint
```

Press Enter.

---

### Step 2: Create Image

Keep:

```text
White Background
```

Use:

```text
Black Color
```

Draw a large handwritten digit.

Example:

```text
7
```

or

```text
1
```

or

```text
8
```

---

### Step 3: Save Image

Select:

```text
File → Save As → PNG Picture
```

Save as:

```text
my_digit.png
```

---

### Step 4: Place Image

Save the image in the same folder as:

```text
main.py
```

Example:

```text
handwritten-digit-recognition/
│
├── main.py
├── my_digit.png
└── README.md
```
## Virtual Environment Troubleshooting

### Problem

If you see errors such as:

```text
ModuleNotFoundError: No module named 'numpy'
```

or

```text
ModuleNotFoundError: No module named 'tensorflow'
```

you are likely using a different virtual environment than the one where the dependencies were installed.

Example:

```text
(.venv)
```

and

```text
(.venv-1)
```

are different environments.

Packages installed in one environment are not automatically available in another environment.

---

### Check Active Environment

Run:

```powershell
where python
```

This displays the Python executable currently being used.

---

### Activate Correct Environment

Deactivate the current environment:

```powershell
deactivate
```

Activate the project environment:

```powershell
.\.venv\Scripts\activate
```

The terminal should display:

```text
(.venv)
```

---

### Verify Installed Packages

Check installed packages:

```powershell
pip list
```

You should see:

```text
numpy
matplotlib
tensorflow
pillow
```

---

### Reinstall Dependencies

If required, install all project dependencies again:

```powershell
pip install numpy matplotlib tensorflow pillow
```

---

### Run the Application

After activating the correct environment:

```powershell
python main.py
```

---

### Important Note

Always activate the same virtual environment before running the project:

```powershell
.\.venv\Scripts\activate
```

Using a different environment may result in missing package errors.

---

## Prediction Output

Example:

```text
Model Accuracy: 97.52%

Predicted Digit : 7
Confidence      : 99.84%
Status          : Correct
```

The application will also display the processed handwritten image.

---

## Tips for Better Predictions

For best results:

* Draw digits large and clear
* Keep the digit centered
* Use a white background
* Use black color for the digit
* Avoid touching image borders
* Avoid very small handwriting
* Save as PNG format

Good Example:

```text
      7
```

Bad Example:

```text
7
```

drawn very small in a large canvas corner.

---

## Neural Network Architecture

Input Layer:

```text
28 × 28 Image
```

Flatten Layer:

```text
784 Features
```

Hidden Layer:

```text
128 Neurons
ReLU Activation
```

Output Layer:

```text
10 Neurons
Softmax Activation
```

---

## Model Performance

Typical Accuracy:

```text
97% – 99%
```

depending on training and testing conditions.

## Author

Handwritten Digit Recognition using MNIST Dataset

Artificial Intelligence Application for recognizing handwritten digits from images.
