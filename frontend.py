# frontend.py
import streamlit as st
from PIL import Image
import numpy as np
import requests

# Alap beállítások
st.title("U-Net alapú kép szegmentáció")

# Kép feltöltés
uploaded_file = st.file_uploader("Tölts fel egy képet", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Feltöltött kép", use_column_width=True)

    # Szegmentációs gomb logikája
    if st.button("Szegmentáció futtatása"):
        # Kép elküldése a Colab API-nak
        # A "http://colab-ip-címe:5000/predict" részt helyettesítsd az ngrok URL-lel, pl.: "http://1234abcd.ngrok.io/predict"
        response = requests.post("http://colab-ip-címe:5000/predict", files={"image": uploaded_file})
        
        if response.status_code == 200:
            result = np.array(response.json()["result"])
            st.image(result, caption="Szegmentált kép", use_column_width=True)
