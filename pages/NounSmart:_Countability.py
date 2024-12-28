import streamlit as st

st.title("NounSmart: Countability")
st.write("How much do you know if a noun is countable or uncountable? Visit this app and check it out.")
st.write("Click the link or scan the QR code to visit the app.")
st.write("Choose a page from the textbook and get all the answers correct.")
st.write("Good luck! 🍀")
st.markdown("Link: [NounSmart: Countability](https://nounsmartcountability-8zeyyjclx4pwyjpfdtmyhk.streamlit.app/)")


import qrcode
from io import BytesIO

# Generate QR code
qr_data = "https://nounsmartcountability-8zeyyjclx4pwyjpfdtmyhk.streamlit.app/"  # Replace with your desired URL or data
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(qr_data)
qr.make(fit=True)


# Convert QR code to an image
qr_image = qr.make_image(fill="black", back_color="white")
buffer = BytesIO()
qr_image.save(buffer, format="PNG")
buffer.seek(0)

# Add QR code to Streamlit
st.image(buffer, caption="Scan this QR code to NounSmart_countability.", use_container_width=True) 
