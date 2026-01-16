import os
import dropbox
from pathlib import Path
import dotenv

ROOT = Path(__file__).resolve().parent.parent
PATH_ENV = ROOT / ".env"

dotenv.load_dotenv(dotenv_path=PATH_ENV)
token = os.getenv("DROPBOX_TOKEN")
if token:
    # Stampa solo i primi 5 caratteri per verifica
    print(f"✅ Token caricato correttamente: {token[:5]}...")
else:
    print("❌ ERRORE: Non sono riuscito a trovare la chiave 'DROPBOX_TOKEN'.")
