"""
Creeremo un programma che andrà automaticamente nella entry e troverà tutti i file Excel e ne unisce il contenuto.
Quindi crea un nuovo file Excel in cui sarà contenuto tutto il contenuto unito.
"""
import os
import pandas as pd

# directory cartella progetto ..\Sezione 12. Merge Excel Files with Python
FOLDER = os.path.dirname(os.path.abspath(__file__)) 
# directori alla sotto cartella ..\Sezione 12...\resources
SUBFOLDER = os.path.join(FOLDER, 'resources') 
# uso una listcomprehension per escludere il file .gitseek 
# e ottenere la lista dei file ['email_addresses1.xlsx', 'email_addresses2.xlsx']
filenames = [f for f in os.listdir(SUBFOLDER) if not f.startswith(".")]
print("Lista dei filenames:",filenames)
filepaths = [os.path.join(SUBFOLDER, filename) for filename in filenames]
print("Percorsi dei filename detti filepaths:",filepaths)
