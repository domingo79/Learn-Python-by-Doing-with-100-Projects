# (1) Il programma carica il file input.xlsx come data frame pandas.
# (2) Calcola e aggiunge una nuova colonna denominata "Total" al data frame.
# La colonna "Totale" è il prodotto ovvero, Prezzo x Quantità.
# (3) Infine, il programma salva il data frame aggiornato in un nuovo file output.xlsx.

import pandas as pd
from pathlib import Path
BASE_DATA = Path(__file__).resolve().parent

file_input = BASE_DATA / "Input.xlsx"
file_output = BASE_DATA / "Output.xlsx"

sales_data = pd.read_excel(file_input)
print("Header:\n", sales_data.head())

# aggiungo colonna Total
sales_data["Total"] = sales_data["Price"] * sales_data["Quantity"]

# ristampo per visualizzare la modifica
print("Visualizzazione mia df con colonna total:\n", sales_data)

# salvo la modifica su un file Output.xlsx
sales_data.to_excel(file_output, index=False)
