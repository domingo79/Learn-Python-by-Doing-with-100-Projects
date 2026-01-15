# Crea un programma Python che acceda all'API Restcountries e stampi informazioni su vari paesi.
# (1) Il programma chiede all'utente di inserire un paese. L'utente digita un paese (ad esempio, Swaziland) e preme Invio
# (2) Il programma stampa la capitale, la regione/continente, la popolazione e le lingue parlate in quel paese.
# The URL endpoint that serves the data is as follows: https://restcountries.com/v3.1/name/{country}
import requests

country = 'Spain'
url = f"https://restcountries.com/v3.1/name/{country}"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    result = response.json()
    if result:
        # prendo il primo risultato della lista
        country_data = result[0]
        # capitali / capitale
        capitali = country_data['capital']
        capitale = capitali[0]
        # popolazione
        popolazione = country_data["population"]
        # regione
        regione = country_data['region']
        # lingue (dict)
        lingue_dict = country_data.get('languages', {})
        lingue = ", ".join(lingue_dict.values()) if lingue_dict else "N/A"
        # larghezza etichette
        W = 12
        # estrapoliamo la valuta
        valute_dict = country_data.get("currencies", {})
        print(
            f" Paese: {country_data.get('name', {}).get('common')} ".center(30, "*"))
        print(f"{'Capitale:':<{W}} {capitale}")
        # La virgola formatta le migliaia
        print(f"{'Regione:':<{W}} {regione}")
        print(f"{'Lingue:':<{W}} {lingue}")
        print(f"{'Popolazione:':<{W}} {popolazione:,}")
        if valute_dict:
            info_valuta = list(valute_dict.values())[0]
            nome_valuta = info_valuta.get('name', 'N/A')
            simbolo_valuta = info_valuta.get('symbol', '')
            print(f"Valuta: {nome_valuta} ({simbolo_valuta})")
        else:
            print("Valuta: Informazione non disponibile")
except requests.exceptions.RequestException as e:
    print(f"ERRORE: {e}")
