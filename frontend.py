import streamlit as st
import requests
import numpy as np
from PIL import Image
import io

st.title("Image Mask Prediction")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type="png")

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Send the image to the API
    url = "http://YOUR_NGROK_URL/predict"  # Replace with Colab's ngrok URL
    files = {'image': uploaded_file}
    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        # Decode mask
        mask_data = np.array(response.json()['mask'], dtype=np.uint8)
        mask = cv2.imdecode(mask_data, cv2.IMREAD_COLOR)
        
        # Display mask
        st.image(mask, caption="Predicted Mask", use_column_width=True)
    else:
        st.error("Prediction failed")
