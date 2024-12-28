import streamlit as st

st.title("NounSmart: Spelling")
st.write("This app is to practice spelling of irregular plural nouns from the textbook.")
st.write("Try to get all the answers correct.")
st.write("Click the link or scan the QR code to visit the app.")
st.write("Good luck! 🍀")
st.markdown("Link: [NounSmart: Spelling](https://nounsmartspelling-hel4hpntntlt56hgphdgw4.streamlit.app/)")

import qrcode
from io import BytesIO

# Generate QR code
qr_data = "https://nounsmartspelling-hel4hpntntlt56hgphdgw4.streamlit.app/"  # Replace with your desired URL or data
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(qr_data)
qr.make(fit=True)


# Convert QR code to an image
qr_image = qr.make_image(fill="black", back_color="white")
buffer = BytesIO()
qr_image.save(buffer, format="PNG")
buffer.seek(0)

# Add QR code to Streamlit
st.image(buffer, caption="Scan this QR code to NounSmart_Spelling.", use_container_width=True) 
