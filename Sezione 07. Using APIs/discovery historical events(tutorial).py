import requests
import calendar
from datetime import datetime


def chiedi_data(message, minimo, massimo):
    while True:
        try:
            valore = int(input(f"{message}: "))
            if minimo <= valore <= massimo:
                return valore
                break
            else:
                print(
                    f"❌ ERRORE: inserisci un numero compreso tra {minimo} e {massimo}.")
        except ValueError:
            print("⚠️  Attenzione: devi inserire un numero, non lettere!")


anno = datetime.now().year
mese = chiedi_data("Inserisci un mese in formato (1-12)", minimo=1, massimo=12)

# calcolo i giorni del mese dopo l'inserimento del mese da parte dell'utente
# monthrange restituisce (giorno_settimana_inizio, numero_giorni_nel_mese)
_, giorni_nel_mese = calendar.monthrange(anno, mese)

giorno = chiedi_data(
    f"Inserisci il giorno in formato ({1}-{giorni_nel_mese})", minimo=1, massimo=giorni_nel_mese)

# da eventi specifici in base al mese/giorno
url_specific_day = f"https://history.muffinlabs.com/date/{mese}/{giorno}"
# url_today = f"https://history.muffinlabs.com/date" → da eventi today

try:
    response = requests.get(url_specific_day, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"ERRORE durante il recupero dei dati: {e}")
    exit()  # evita una reazione a catena di errori.

# il nostro paracadute:
# "Cerca questa chiave. Se la trovi, dammi il suo valore. Se NON la trovi, non dare errore,
# ma dammi quello che c'è dopo la virgola."
events = data.get("data", {}).get("Events", [])

# stampa risultati
print(f"\n--- Eventi storici del {giorno}/{mese} ---\n")
for event in events:
    print(f" 📅 Anno: {event['year']}")
    print(f" 📝 {event['text']}")

    # mostriamo i titoli dei link in modo più compatto
    links = [link['title'] for link in event.get('links', [])]
    if links:
        print(f" 📎Approfondisci: {', '.join(links)}")
    print("-" * 30)
