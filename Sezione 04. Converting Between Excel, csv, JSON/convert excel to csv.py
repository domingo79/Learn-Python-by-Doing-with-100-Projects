# libreria suggerita `Pandas` e per la gestione dei file excel `openpyxl`
# dalla documentazioni di Pandas suggeriva appunto l'installazione includendo la dipendenza per la lettura di file Excel:
# pip install "pandas[excel]"

# Creare un programma che converte un file excel in un file CSV.
# leggi il file europe.xlsx e salvi convertendo in europe.csv nella stessa directory dello script.
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_excel = BASE_DIR / "europe.xlsx"
file_csv = BASE_DIR / "europe.csv"

# legge il file excel
df = pd.read_excel(file_excel)

# converte il df in csv file
df.to_csv(file_csv, index=False, sep=",")
