import streamlit as st
from PIL import Image

st.set_page_config(page_title="Remote Radiologist", layout="wide", initial_sidebar_state="expanded")

header = st.beta_container()

description = st.beta_container()

user_inputs = st.beta_container()


with header:
    header.title("Remote Radiologist")


with user_inputs:
    user_display, output_display = user_inputs.beta_columns(2)
    pat_name = user_display.text_input("Name of the Patient")
    pat_age = user_display.number_input("Age of the Patient", 5, 90)
    pat_weight = user_display.number_input("Weight in KGs", 30, 150)
    pat_gender = user_display.selectbox('Gender', ('Male', 'Female', 'Others'))
    uploaded_file = output_display.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        output_display.image(image, caption='Uploaded Image.', use_column_width=True)
        # labels = {'Covid%': 35, 'XYZ': 35, 'ABC': 30}
        labels = {}
        # call the predictor here
        for key, value in labels.items():
            output_display.write(key + " : " + str(value))


