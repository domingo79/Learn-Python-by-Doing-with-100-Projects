"""
Creamo un programma che conta le fequenze delle parola utilizzando tutti i file.txt
contenuto nella cartella resources
"""
import os

FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCES = os.path.join(FOLDER, 'resources')
OUTPUT = os.path.join(FOLDER, 'output')
