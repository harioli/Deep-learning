# -*- coding: utf-8 -*-
"""streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u1UTNBgBzrHQBoCwsNnYZhniryyk3776
"""

# pip install streamlit

# from google.colab import drive
# drive.mount('/content/drive')



import streamlit as st
import numpy as np
import cv2
from keras.models import load_model

# Load the trained model
model = load_model('/content/drive/MyDrive/Colab Notebooks.h5')  # Replace with your model file path



# Define class labels
class_labels = {
    0: "airplane",
    1: "automobile",
    2: "bird",
    3: "cat",
    4: "deer",
    5: "dog",
    6: "frog",
    7: "horse",
    8: "ship",
    9: "truck"
}

# Create a Streamlit app
st.title("CIFAR-10 Image Classification App")

# Upload an image
st.write("Upload an image for classification:")
uploaded_image = st.file_uploader('/content/bird.jpg')

if uploaded_image is not None:
    # Display the uploaded image
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # Preprocess and make predictions
    image = cv2.imread(uploaded_image.name)
    image = cv2.resize(image, (32, 32), interpolation=cv2.INTER_CUBIC)
    image = np.reshape(image, (1, 32, 32, 3)) / 255.0

    prediction = model.predict(image)
    class_num = np.argmax(prediction)

    st.write("Prediction:")
    st.write(f"Class: {class_labels[class_num]}")
    st.write(f"Confidence: {prediction[0][class_num]:.2%}")

import streamlit as st

# Your Streamlit app code
st.title('My Streamlit App')
st.write('Welcome to my Streamlit app!')

# Run the app

