"""Convertitore di valuta USD ⮂ EUR"""
import streamlit as st
import requests

try:
    if "EXCHANGE_RATE_KEY" in st.secrets:
        # Gestione sicura dei segreti
        api_key = st.secrets["EXCHANGE_RATE_KEY"]
    else:
        raise KeyError
except (FileNotFoundError, KeyError, RuntimeError):
    st.error("### ⚠️ Attenzione: Configurazione Ambiente non completata")
    st.info("""
        Non è stato possibile individuare le credenziali API necessarie per il funzionamento dell'app.

        **Per risolvere:**
        1. Vai nella cartella `.streamlit/`
        2. Copia il file `secrets.toml.example` e nominalo `secrets.toml`
        3. Inserisci la tua API Key nel file appena creato.
    """)
    st.stop()


def convert(da_valuta, a_valuta, importo):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{da_valuta}"
    try:
        response = requests.get(url=url, timeout=10)
        response.raise_for_status()  # Controlla che il download sia andato a buon fine
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"ERRORE durante il recupero dei dati: {e}")
        exit()  # evita una reazione a catena di errori.

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
