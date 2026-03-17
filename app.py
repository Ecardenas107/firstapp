import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR Code Generator")

st.title("QR Code Generator")
st.write("Enter text or a URL to generate a QR code.")

data = st.text_input("Enter text or URL", "Python is fun")

if data:
    qr = qrcode.make(data)
    buf = BytesIO()
    qr.save(buf, format="PNG")
    st.image(buf.getvalue(), caption="Generated QR Code")
