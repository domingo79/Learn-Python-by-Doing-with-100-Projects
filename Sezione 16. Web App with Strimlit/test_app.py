import streamlit as st
import pandas as pd  # Utile per le tabelle

# Titolo dell'app
st.title("Word Frequency Analyzer 📊")

# Immagina di avere il tuo dizionario word_frequency
word_frequency = {"python": 25, "codice": 15, "studio": 10}

# Visualizzare i dati come tabella
st.subheader("Tabella delle frequenze")
st.write(word_frequency)

# Visualizzare i dati come grafico a barre (fighissimo e immediato)
st.subheader("Grafico a barre")
st.bar_chart(word_frequency)

# Un bottone per scaricare il file
st.download_button(
    label="Scarica i risultati",
    data=str(word_frequency),
    file_name="word_frequencies.txt"
)

# per avviare → streamlit run app.py
