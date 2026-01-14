# creeremo un programma da riga di comando(CLI) per un To-do list
# terminato l'inserimento dei vari todo tramile la parole `done` il programma deve salvare il file e terminare
# il file salvato avrà il nome del giorno della data attuale .txt
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent
GIORNI_IT = {
    "Monday": "lunedì",
    "Tuesday": "martedì",
    "Wednesday": "mercoledì",
    "Thursday": "giovedì",
    "Friday": "venerdì",
    "Saturday": "sabato",
    "Sunday": "domenica"
}
adesso = datetime.now()
day = adesso.strftime("%A")
giorno_it = GIORNI_IT[day]
FILE_OUTPUT = DATA_DIR / f"{giorno_it}.txt"


def salva(lista):
    # controllare se la lista è vuota
    if not lista:
        print("Lista vuota, nulla da salvare.")
        return

    with open(FILE_OUTPUT, "w", encoding="utf-8") as f:
        f.write(
            f"--- TODO DEL GIORNO: {giorno_it.upper()} ({adesso.strftime('%d/%m/%Y')}) ---\n")
        for todo in lista:
            # Aggiungo il punto e l'andata a capo ad ogni todo
            f.write(f"- {todo}.\n")
    print(f"\n✅ File `{FILE_OUTPUT.name}` salvato con successo!")
    print(f"Hai sdalvato {len(lista)} impegni.")


todo_list = []
# Output di benvenuto migliorato
print("="*55)
print(" 📝 IL TUO GESTORE TODO ".center(55, ' '))
print("="*55)
print("👉 Inserisci un impegno alla volta e premi INVIO.")
print("👉 Puoi inserirne quanti ne vuoi.")
print("👉 Quando hai finito, digita 'done' per salvare e uscire.")
print("-"*55)

while True:
    user_input = input("> ").strip()

    # uscita con la parola done
    if user_input.lower() == 'done':
        salva(todo_list)
        break
    # evita una riga vuota
    if user_input:
        todo_list.append(user_input.capitalize())
