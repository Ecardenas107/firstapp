import streamlit as st
import qrcode

st.title("QR Code Generator")

data = st.text_input("Enter text or URL", "Python is fun ")

if data =
    img = qr.code.make(data)
    st.image(img)
