import streamlit as st
import requests

# Az ngrok URL manuális megadása
public_url = st.text_input("Add meg az ngrok URL-t (pl. https://xxxx-xx-xx-xx.ngrok.io)")

# Kép feltöltése és API hívás
uploaded_file = st.file_uploader("Tölts fel egy képet", type=["jpg", "jpeg", "png"])

if public_url and uploaded_file is not None:
    files = {"image": uploaded_file}
    response = requests.post(f"{public_url}/predict", files=files)

    if response.status_code == 200:
        result = response.json()
        st.write("Predikció eredménye:", result)
    else:
        st.write("Hiba történt a predikció során.")
