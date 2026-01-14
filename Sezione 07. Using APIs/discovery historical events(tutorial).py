import requests
import calendar
from datetime import datetime

anno = datetime.now().year
mese = datetime.now().month
# monthrange restituisce (giorno_settimana_inizio, numero_giorni_nel_mese)
_, giorni_nel_mese = calendar.monthrange(anno, mese)

while True:
    try:
        mounth = int(input("Inserisci mese (1-12): "))

        if 1 <= mounth <= 12:
            break  # Esci dal ciclo se il numero è corretto
        else:
            print("❌ Errore: il mese deve essere compreso tra 1 e 12.")

    except ValueError:
        print("⚠️  Attenzione: devi inserire un numero, non lettere!")


while True:
    try:
        day = int(input(f"Inserisci giorno (1-{giorni_nel_mese}): "))

        if 1 <= day <= giorni_nel_mese:
            break  # Esci dal ciclo se il numero è corretto
        else:
            print(
                f"❌ Errore: il giorno deve essere compreso tra 1 e {giorni_nel_mese}.")

    except ValueError:
        print("⚠️  Attenzione: devi inserire un numero, non lettere!")


url_specific_day = f"https://history.muffinlabs.com/date/{mounth}/{day}"
url_today = f"https://history.muffinlabs.com/date"

try:
    response = requests.get(url_specific_day, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"ERRORE durante il recupero dei dati: {e}")
    exit()  # evita una reazione a catena di errori.

events = data["data"]["Events"]
for event in events:
    print(f"Anno: {event['year']}")
    print(f"Descrizione: {event['text']}")
    print("Link Utili:")
    for link in event['links']:
        print(f"\tTitolo: {link['title']}")
        print(f"\tLink: {link['link']}")
    print("\n")
