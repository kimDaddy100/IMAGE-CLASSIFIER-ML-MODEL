import cv2 
import numpy as np
import streamlit as st
from tensorflow.keras.application.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from PIL import Image
def load_model():
    model = MobileNetV2(weights="imagenet")
    return model
def preprocess_image(image):
    img = np.array(image)
    img = cv2.resize(img(224,224))
    img = preprocess_input(img)
    