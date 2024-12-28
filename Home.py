import streamlit as st

st.title("Welcome to Sundaybest's Home!")
         
import streamlit as st
from PIL import Image

# Load the resized pastel-toned image
image_path = "https://github.com/sundaybest3/sundaybest/blob/main/home_image.png"  # Adjust this path
image = Image.open(image_path)

# Display the image in Streamlit
st.image(image, caption="Pastel Toned Image", use_container_width=True)
