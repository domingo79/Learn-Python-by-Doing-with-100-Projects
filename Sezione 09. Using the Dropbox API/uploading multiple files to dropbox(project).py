# Requisito di projetto:
# creare un script che funga da API Request al servizio dropbox per caricare dei
# file mediante l'uso di un ciclo

import os
import dropbox
from pathlib import Path
import dotenv

# percorsi cartella root e file
CARTELLA = Path(__file__).resolve().parent
ROOT = CARTELLA.parent
PATH_ENV = ROOT / ".env"
CARTELLA_FILES = CARTELLA / "files"

# cerca e associa token
dotenv.load_dotenv(dotenv_path=PATH_ENV)
token = os.getenv("DROPBOX_TOKEN")
if token:
    # Stampa solo i primi 5 caratteri per verifica
    print(f"✅ Token caricato correttamente: {token[:5]}...")
else:
    print("❌ ERRORE: Non sono riuscito a trovare la chiave 'DROPBOX_TOKEN'.")

# accesso a dropbox
dbx = dropbox.Dropbox(token)

# uploaded img tramite ciclo
for file_path in CARTELLA_FILES.glob("*"):
    # controlliamo che sia un file e non una cartella
    if file_path.is_file():
        file_name = file_path.name
        print(f"Preparazione upload di: {file_name}")
        try:
            with open(file_path, "rb") as f:
                content = f.read()
                # Usiamo f'/{file_name}' per mantenere lo stesso nome file
                dbx.files_upload(
                    content, f'/{file_name}', mode=dropbox.files.WriteMode('overwrite'))
                print(f" ✅ File {file_name} uploaded successfully!")
        except Exception as e:
            print(f" ❌ ERRORE durante l'upload di {file_name}: {e}")
