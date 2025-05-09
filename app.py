import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="PNG 圖片檢視",
    layout="wide",
)
st.title("PNG 圖片檢視：有無 alpha 透明度")

# Upload the PNG file
uploaded_file = st.file_uploader("上傳 PNG 圖片", type=["png"])

if uploaded_file is not None:
    # Open image with PIL
    image = Image.open(uploaded_file).convert("RGBA")  # ensure RGBA

    # Remove alpha channel
    image_rgb = image.convert("RGB")

    # Layout: Show side by side
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("原始圖片 (有 alpha 透明度)")
        with st.container(border=True):
            st.image(image)

    with col2:
        st.subheader("Alpha 移除 (RGB 純色)")
        with st.container(border=True):
            st.image(image_rgb)
