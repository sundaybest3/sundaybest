import streamlit as st

st.title("Welcome to Sundaybest's Home!")

# Raw URL 사용
image_url = "https://raw.githubusercontent.com/sundaybest3/sundaybest/main/home_image.png"

st.image(image_url, caption="Home Image", use_container_width=True)
