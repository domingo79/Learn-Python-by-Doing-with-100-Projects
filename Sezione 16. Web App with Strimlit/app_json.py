"""
converte un file excel in file.json
"""
from utility import convert_excel_to_JSON
import streamlit as st

st.title(':blue[Excel] to :red[JSON converter]')
st.write("Upload an Excel file to convert in to JSON format")

uploaded_file = st.file_uploader("Chose an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    json_data = convert_excel_to_JSON(uploaded_file)

    st.json(json_data)

    st.download_button(label="Dowload JSON",
                       data=json_data,
                       file_name="converted.json",
                       mime='application/json'
                       )
