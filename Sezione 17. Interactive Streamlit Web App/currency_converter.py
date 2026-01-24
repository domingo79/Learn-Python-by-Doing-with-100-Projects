import streamlit as st
import requests


api_key = st.secrets["EXCHANGE_RATE_KEY"]
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"


def convert(valuta, importo):
    response = requests.get(url=url, timeout=10)
    data = response.json()

    return data


st.title(":blue[Convertitore] di :red[Valuta:] USD ⮂ EUR")

conversion = st.radio("Scegli la conversione:", ("USD a EUR", "EUR a USD"))

input_valur = st.number_input("Inserisci l'importo da convertire")

button = st.button("Converti", disabled=False)

if conversion == 'USD a EUR':
    if button:
        euros = convert(conversion[:3], input_valur)
        st.success(f"Il risulato della conversione è {euros}")
else:
    if button:
        dollars = convert(conversion[:3], input_valur)
        st.success(f"Il risulato della conversione è {dollars}")
