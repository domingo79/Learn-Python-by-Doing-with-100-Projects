import os
import dropbox
from pathlib import Path
import dotenv

# percorsi cartella root e file
CARTELLA = Path(__file__).resolve().parent
ROOT = CARTELLA.parent
PATH_ENV = ROOT / ".env"
chicago_img = CARTELLA / "chicago.jpg"

# cerca token
dotenv.load_dotenv(dotenv_path=PATH_ENV)
token = os.getenv("DROPBOX_TOKEN")
if token:
    # Stampa solo i primi 5 caratteri per verifica
    print(f"✅ Token caricato correttamente: {token[:5]}...")
else:
    print("❌ ERRORE: Non sono riuscito a trovare la chiave 'DROPBOX_TOKEN'.")

# accesso a dropbox
dbx = dropbox.Dropbox(token)
file_name = 'chicago.jpg'

# accesso all'immagine
with open(chicago_img, "rb") as f:
    content = f.read()
    # uploaded img
    dbx.files_upload(content, f'/{file_name}',
                     mode=dropbox.files.WriteMode('overwrite'))
    print(f"File {file_name} uploaded successfully!")
