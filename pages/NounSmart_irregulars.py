import streamlit as st

st.title("NounSmart: irregulars")
st.write("This is an app you can use to practice irregular plural nouns. Click the link or scan the QR code to visit the page!") 
st.write("Link: https://nounsmartirregulars-5xvnwrz796lsebgkjmyotk.streamlit.app/")

import qrcode
from io import BytesIO

# Generate QR code
qr_data = "https://your-link-here.comhttps://nounsmartirregulars-5xvnwrz796lsebgkjmyotk.streamlit.app/"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(qr_data)
qr.make(fit=True)

# Convert QR code to an image
qr_image = qr.make_image(fill="black", back_color="white")
buffer = BytesIO()
qr_image.save(buffer, format="PNG")
buffer.seek(0)

st.image("path/to/qr_code.png", caption="Scan this QR code to visit our page!", use_column_width=True)


