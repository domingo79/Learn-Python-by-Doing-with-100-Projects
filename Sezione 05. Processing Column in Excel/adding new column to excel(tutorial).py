# in questo tutorial aggiungeremo una colonna `bonus` al file excel
# la colonna bonus includerà il 10% dello stipendio (0.1)
from pathlib import Path
import pandas as pd

BASE_DATA = Path(__file__).resolve().parent
file_input = BASE_DATA / "employee_data.xlsx"
file_output = BASE_DATA / "employee_data_bonus.xlsx"

# Forza la visualizzazione di tutte le colonne senza andare a capo
pd.set_option('display.expand_frame_repr', False)

employee_data = pd.read_excel(file_input)
# Ispezionare i dati (Cosa c'è dentro?) Prima di lavorare, devi capire cosa hai caricato.
# df.head(): Mostra le prime 5 righe.
print(employee_data.head())
# df.info(): Ti dice i nomi delle colonne, quanti dati mancano e il tipo di dati (numeri, stringhe, date).
print(employee_data.info())
# df.describe(): Calcola statistiche veloci (media, minimo, massimo) per le colonne numeriche.
print(employee_data.describe())
# df.columns: Ti restituisce la lista dei nomi delle colonne.
print(employee_data.columns)

# AGGIUNGO LA COLONNA Bonus come se fosse un dict
employee_data['Bonus'] = employee_data['Salary'] * 0.1

# scivo il nuovo file
employee_data.to_excel(file_output, index=False)
