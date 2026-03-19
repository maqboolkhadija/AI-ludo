import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.title("AI Ludo Game")

# Step 2: File uploader for board image
uploaded_file = st.file_uploader("Upload your Ludo board image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load uploaded image
    board_image = Image.open(uploaded_file)
    st.image(board_image, caption="Ludo Board", use_column_width=True)

    # Canvas setup with uploaded image as background
    canvas_result = st_canvas(
        fill_color="rgba(0,0,0,0)",   # transparent initially
        stroke_width=2,
        stroke_color="#000000",
        background_image=board_image,
        height=500,
        width=500,
        drawing_mode="freedraw",
        key="canvas",
    )

    # Show canvas output
    if canvas_result.image_data is not None:
        st.image(canvas_result.image_data, caption="Canvas Output")
else:
    st.warning("Please upload the board image to start.")
