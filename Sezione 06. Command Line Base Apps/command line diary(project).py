# (1) Il programma chiede all'utente di inserire le proprie note.
# (2) Se l'utente digita il testo "exit", il programma esce e salva le note in un file di testo.
# Il nome del file di testo deve contenere il giorno corrente della settimana (ad esempio, Thursday.txt).
# (3) Il programma visualizza un messaggio che informa l'utente che le note sono state salvate in un file.
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).resolve().parent
adesso = datetime.now()
day = adesso.strftime("%A")
filename = DATA_DIR / f"{day}.txt"
diary_list = []


def salva_diario(lst):
    if not lst:
        print("Nessusa nota da salvare!")
        return

    with open(filename, "w", encoding="utf-8") as f:
        f.write(
            f"--- DIARIO DEL GIORNO: {day.upper()} ({adesso.strftime('%d/%m/%Y')}) ---\n")
        for pensiero in lst:
            f.write(f"{pensiero}.\n")
    print(f"✅ File `{filename.name}` salvato con successo!")
    print(f"Sono stati aggiunti {len(lst)} pensieri😉")


# Output di benvenuto/presentazione
print("="*60)
print("📝 IL TUO DIARIO ".center(60, ' '))
print("="*60)
print("👉 Inserisci un pensiero alla volta e premi INVIO.")
print("👉 Puoi inserirne tutti i tuoi segreti.")
print("👉 Quando hai finito, digita 'exit' per salvare e uscire.")
print("-"*60)

while True:
    user_input = input("> ").strip()

    # controlla e salva in caso di uscita
    if user_input.lower() == "exit":
        salva_diario(diary_list)
        break

    # evita di salvare righe vuote
    if user_input:
        diary_list.append(user_input.capitalize())
