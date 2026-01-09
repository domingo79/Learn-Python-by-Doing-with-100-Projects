# Crea un programma Python che rinomini in batch più file.
# per questo progetto bisogna creare una cartella files e all'nterno alcuni file.txt
# Il programma deve rinominare ogni file aggiungendo la data corrente nel formato AAAA-MM-DD ai nomi dei file.
# Più specificamente, i file dovrebbero apparire come segue dopo l'esecuzione del programma. "a-2026-01-09.txt"
# il programma dovrebbe stampare alcuni messaggi nel terminale per informare l'utente che i file sono stati rinominati:
# >>> Renamed 'a.txt' to 'a-2026-01-09.txt'
# >>> File ranaming completed.
# Suggested Libraries os and datetime

import os
from datetime import datetime

# definiamo la data con fornato YYYY-MM-DD
data_oggi = datetime.now().strftime("%Y-%m-%d")

# OTTENIAMO IL PERCORSO DELLA CARTELLA DOVE RISIEDE QUESTO SCRIPT:
script_dir = os.path.dirname(os.path.abspath(__file__))

# definiamo il percorso della nostra cartella target:'files'
cartella_target = os.path.join(script_dir, "files")

# verifichiamo l'esistenza della cartella
if os.path.exists(cartella_target):

    # elenchiamo i file contenuti nella cartella target
    percorsi_file = os.listdir(cartella_target)

    for nome_file in percorsi_file:
        # Costruiamo il percorso completo del file originario (es: "files/a.txt")
        vecchio_percorso = os.path.join(cartella_target, nome_file)
        # verifichiamo che sia un file e non una cartella
        if os.path.isfile(vecchio_percorso) and nome_file.endswith(".txt"):
            # piccola fix per non modificare il file se ha già la data di oggi
            if data_oggi in nome_file:
                print(f"Skipped `{nome_file}` (data già presente)")
                continue

            # splitto nome ed estensione
            nome_puro, estensione = os.path.splitext(nome_file)

            # Creiamo il nuovo nome: a + - + data + .txt
            nuovo_nome = f"{nome_puro}-{data_oggi}{estensione}"
            nuovo_percorso = os.path.join(cartella_target, nuovo_nome)

            # rinominiamo fisicamente il file
            os.rename(vecchio_percorso, nuovo_percorso)
            print(f"Renamed '{nome_file}' to `{nuovo_nome}`")
    print("File ranaming completed.")
else:
    print(f"ERRORE: La cartella `{cartella_target}` non è stata trovata!")
