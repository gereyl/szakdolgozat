import requests
import streamlit as st
from PIL import Image

st.title("U-Net Szegmentáció")
uploaded_file = st.file_uploader("Kép feltöltése", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Eredeti kép", use_column_width=True)
    
    if st.button("Szegmentáció"):
        # Küldd el az API-hoz
        files = {"image": uploaded_file.getvalue()}
        response = requests.post("http://<ngrok-URL>/predict", files=files)
        
        if response.status_code == 200:
            result_image = Image.open(io.BytesIO(response.content))
            st.image(result_image, caption="Szegmentált kép", use_column_width=True)
        else:
            st.write("Hiba történt a szegmentáció során.")
