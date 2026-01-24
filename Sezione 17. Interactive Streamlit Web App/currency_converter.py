"""Convertitore di valuta USD ⮂ EUR"""
import streamlit as st
import requests

api_key = st.secrets["EXCHANGE_RATE_KEY"]


def convert(da_valuta, a_valuta, importo):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{da_valuta}"

    response = requests.get(url=url, timeout=10)
    data = response.json()

    tasso = data['conversion_rates'][a_valuta]
    result = importo * tasso
    return result


st.title(":blue[Convertitore] di :red[Valuta:] USD ⮂ EUR")

conversion = st.radio("Scegli la conversione:", ("USD a EUR", "EUR a USD"))

input_valur = st.number_input("Inserisci l'importo da convertire")

button = st.button("Converti", disabled=False)

if button:
    # Estraiamo le valute una volta sola
    da_val = conversion[:3]
    a_val = conversion[-3:]
    # Chiamiamo la funzione (che ora gestisce l'URL dinamico)
    risultato = convert(da_val, a_val, input_valur)
    # Mostriamo il risultato usando il tuo simbolo speciale
    st.success(f"{input_valur} {da_val} ⮂ {risultato:.2f} {a_val}")
