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
    if conversion == "USD a EUR":
        da_val = conversion[:3]
        a_val = conversion[-3:]
        risultato = convert(da_val, a_val, input_valur)
    else:
        da_val = conversion[:3]
        a_val = conversion[-3:]
        risultato = convert(da_val, a_val, input_valur)
    st.success(
        f"{input_valur} {da_val} equivalgono a: {risultato:.2f} {a_val}")
