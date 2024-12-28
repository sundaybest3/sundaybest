import streamlit as st
import qrcode
from io import BytesIO

# Generate QR code
qr_data = "https://your-link-here.com"  # Replace with your desired URL or data
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(qr_data)
qr.make(fit=True)

# Convert QR code to an image
qr_image = qr.make_image(fill="black", back_color="white")
buffer = BytesIO()
qr_image.save(buffer, format="PNG")
buffer.seek(0)

# Add QR code to Streamlit
st.image(buffer, caption="Scan this QR code to visit our page!", use_column_width=True)


