"""
Creeremo un programma che andrà automaticamente nella entry e troverà tutti i file Excel e ne unisce il contenuto.
Quindi crea un nuovo file Excel in cui sarà contenuto tutto il contenuto unito.
"""
import os
import pandas as pd

# ---- GESTIONE CARTELLE IN ENTRATA -----

# directory cartella progetto ..\Sezione 12. Merge Excel Files with Python
FOLDER = os.path.dirname(os.path.abspath(__file__)) 
# directori alla sotto cartella ..\Sezione 12...\resources
SUBFOLDER = os.path.join(FOLDER, 'resources') 
# uso una listcomprehension per escludere il file .gitseek e ottenere la lista dei file
filenames = [f for f in os.listdir(SUBFOLDER) if not f.startswith(".")]
# otteniamo i file paths
filepaths = [os.path.join(SUBFOLDER, filename) for filename in filenames]

# ---- LEGGIAMO I FILE E CREAMO UNA LISTA DI FILE ALL'INTERMO DEL DATAFRAME -----

# leggiamo i file excel con pandas
dataframes = [pd.read_excel(filepath) for filepath in filepaths]

# ---- CONCATENIAMO IN DF IN UN MERGE DF -----

# concateniamo il dataframe in un unico merget_df
# ignore_index=True perchè il df crea una colonna index che non vogliamo come colonna nel file excel
merged_df = pd.concat(dataframes, ignore_index=True)

# ---- GESTIONE CARTELLE IN OUTPUT -----

# costruiamo il path del file excel mergiato
OUTPUT = os.path.join(FOLDER, 'output') 
file_name = 'merged.xlsx'
merged_path = os.path.join(OUTPUT, file_name)

# ---- ESPORTIAMO IN MERGE DATA FRAME -----
# index=False per non creare colonne index
merged_df.to_excel(merged_path, index=False)