"""
Crea un programma che unisca file di testo.
(1) Quando l'utente avvia il programma, il programma deve scorrere tutti i file 
con estensione txt dalla cartella resources.
(2) Poi il programma deve salvare il contenuto dei file in uno nuovo file e salvarlo.
"""
import os
from glob import glob

FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCES = os.path.join(FOLDER, 'resources')
OUTPUT = os.path.join(FOLDER, 'output')
SAVE_FILE = os.path.join(OUTPUT, 'merge_file.txt')
file_paths = glob(f"{RESOURCES}/*.txt")

merge_file = ''

for filepath in file_paths:
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        merge_file += content

with open(SAVE_FILE, 'w', encoding='utf-8') as file:
    if merge_file:
        file.write(merge_file)
        print(f"File salvato con successo in {os.path.basename(SAVE_FILE)}")
