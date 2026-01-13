import requests
URL = "https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json"

# la funzione get() recupera i dati da un URL specifico
try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()  # Controlla che il download sia andato a buon fine
    quiz_data = response.json()
except requests.exceptions.RequestException as e:
    print(f"ERRORE durante il recupero dei dati: {e}")
    exit()  # evita una reazione a catena di errori.

# gestione sicura dell'input ID
try:
    question_id = int(input("Inserisci il numero di domanda: "))
except ValueError:
    print("Inserisci un numero valido!")
    exit()  # evita una reazione a catena di errori.

# variabili di controllo e funzionamento
risposta_corretta = None
domanda_trovata = None
opzioni = []

for quiz in quiz_data["quizzes"]:
    for question in quiz["questions"]:
        if question["id"] == question_id:
            domanda_trovata = question["question"]
            for k, v in question["choices"].items():
                opzioni.append(k)
                if v == True:
                    risposta_corretta = k.lower()
            break
    if domanda_trovata:
        break

# se l'id inserito corrisponde ad una domanda proseguo altrimenti termino
if domanda_trovata:
    # stampiamo domanda e le relative opzioni
    print(f"DOMANDA: {domanda_trovata}")
    for opzione in opzioni:
        print(f"- {opzione}")

    # chiediamo la risposta
    risposta = input("Scrivi la tua risposta: ").lower().strip()

    # controlliamo la risposta
    if risposta_corretta == risposta:
        print("Perfetto! Hai indovinato")
    else:
        print("Asinello!!!")
else:
    print(f"ID `{question_id}` non trovato")
