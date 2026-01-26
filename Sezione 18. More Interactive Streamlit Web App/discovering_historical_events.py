"""
Crea un'app Web che consenta agli utenti di visualizzare gli eventi storici per un determinato giorno dell'anno.
(1) Il programma consente all'utente di immettere un numero di mese (ad esempio, 10 per ottobre) e un giorno (ad esempio, 25).
(2) Il programma estrae tutti gli eventi storici* per quella data e li visualizza sulla pagina web.
endpoint: http://history.muffinlabs.com/date/{month}/{day}. For example:  http://history.muffinlabs.com/date/10/25
"""
import requests
import streamlit as st

st.title(":red[Visualizzatore] di :blue[eventi storici]")
st.text("Inserisci una data per recuperare gli eventi storici")
month = st.number_input("Inserisci il mese (es. 10 per ottobre)",
                        min_value=1, max_value=12, step=1, value=1)
# Logica per determinare i giorni massimi
if month in [4, 6, 9, 11]:
    max_d = 30
elif month == 2:
    # Per semplicità gestiamo 29, o potresti aggiungere il selettore anno per i bisestili
    max_d = 29
else:
    max_d = 31

day = st.number_input("Inserisci il giorno (es. 1 per il primo giorno del mese)",
                      min_value=1, max_value=max_d, step=1, value=1)

endpoint = f"http://history.muffinlabs.com/date/{month}/{day}"
try:
    response = requests.get(endpoint, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"ERRORE durante il recupero dei dati: {e}")
    exit()

# "Cerca questa chiave. Se la trovi, dammi il suo valore. Se NON la trovi, non dare errore,
# ma dammi quello che c'è dopo la virgola."
events = data.get("data", {}).get("Events", [])
eventi_ordinati = sorted(events, key=lambda x: int(x['year']), reverse=True)

if st.button("Mostra Eventi", type='secondary'):
    # stampa risultati
    st.write(f"--- Eventi storici del {day}/{month} ---\n")
    for event in eventi_ordinati:
        st.write(f" 📅 Anno: {event['year']}")
        st.write(f" 📝 {event['text']}")
        st.write("-" * 30)
