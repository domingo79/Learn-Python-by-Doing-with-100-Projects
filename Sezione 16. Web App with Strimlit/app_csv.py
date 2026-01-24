"""
converte un file excel in file.csv
"""
from utility import convert_excel_to_csv
import streamlit as st

st.title(":blue[Excel] to :red[CSV] converter")
st.write("Upload an :blue[Excel file] to convert it to :red[CSV] format.")

uploaded_file = st.file_uploader("Choose a Excel file")

if uploaded_file is not None:
    # 1. Chiedi all'utente il nome del file
    file_name = st.text_input(
        label="Inserisci il nome del file di output (senza estensioni)",
        value="file_convertito"
    )
    # Assicuriamoci che il nome finisca con .csv
    if not file_name.endswith('.csv'):
        full_file_name = f"{file_name}.csv"
    else:
        full_file_name = file_name

    csv_data = convert_excel_to_csv(uploaded_file)

    st.download_button(
        label="Press to Download CSV",
        data=csv_data,
        file_name=full_file_name,
        mime="text/csv",
        key='download-csv'
    )
