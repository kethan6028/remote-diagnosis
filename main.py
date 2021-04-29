import streamlit as st
from PIL import Image
header = st.beta_container()

description = st.beta_container()

user_inputs = st.beta_container()


with header:
    header.title("Remote Radiologist")

# with description:
#     description.subheader("Project Description")
#     description.text("Write the Project Description Here!!!")

with user_inputs:
    user_col, display_col = st.beta_columns(spec=2)
    uploaded_file = st.file_uploader("Upload Image", type=['png', 'jpg', 'pdf', 'jpeg'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        # labels = {'Covid%': 35, 'XYZ': 35, 'ABC': 30}
        labels = {}
        # call the predictor here
        for key, value in labels.items():
            st.write(key + " : " + str(value))


