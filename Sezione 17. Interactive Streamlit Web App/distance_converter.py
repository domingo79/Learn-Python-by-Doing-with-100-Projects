"""
Questa applicazione permette di convertire km ⮂ Miglia
e non solo:
Da,  A,   Moltiplica per
km,  mi,  0.621371
mi,  km,   1.60934
m,  ft,    3.28084
ft,  m,    0.3048
"""
import streamlit as st


def convert(scelta, valore):
    conversioni = {
        "km a mi": 0.621371,
        "mi a km": 1.60934,
        "m a ft": 3.28084,
        "ft a m": 0.3048
    }
    moltiplicatore = conversioni.get(scelta)
    return valore * moltiplicatore


st.title("📏 Convertitore di distanze")
st.header("Scegli la tua conversione preferita:")

opzioni = ("km a mi", "mi a km", "m a ft", "ft a m")
user_input = st.radio("Seleziona la conversione:", opzioni)

distanza = st.number_input("Inserisci il valore da convertire", min_value=0.0)

if st.button("Converti"):
    risultato = convert(user_input, distanza)
    # Estraiamo le unità per il messaggio finale
    unita_da = user_input.split(" a ")[0]
    unita_a = user_input.split(" a ")[1]
    st.success(
        f"{distanza} {unita_da} equivalgono a: {risultato:.4f} {unita_a}")
