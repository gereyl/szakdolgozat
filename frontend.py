# frontend.py
import streamlit as st
from PIL import Image
import numpy as np

# Alap beállítások
st.title("U-Net alapú kép szegmentáció")

# Kép feltöltés
uploaded_file = st.file_uploader("Tölts fel egy képet", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Feltöltött kép", use_column_width=True)

    # Küldd el az API-nak a képet a szegmentáláshoz
    if st.button("Szegmentáció futtatása"):
        # Kép előfeldolgozása és predikciós lekérdezés küldése itt történik
        pass
