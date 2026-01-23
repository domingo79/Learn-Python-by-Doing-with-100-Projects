"""
Creamo un programma che conta le fequenze delle parola utilizzando tutti i file.txt
contenuto nella cartella resources e poi salviamo le frequenze su un nuovo file
"""
import os
from glob import glob

FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCES = os.path.join(FOLDER, 'resources')
OUTPUT = os.path.join(FOLDER, 'output')
# glob ci permette di ottenere il percorso, possiamo anche ordinarlo
filepaths = sorted(glob(f"{RESOURCES}/*.txt"))
save_frequences = os.path.join(OUTPUT, 'word_frequencies.txt')


def remuve_punctuaction(text):
    """Rimuove i caratteri speciali dal testo

    Args:
        text (str): testo inserito dall'utente

    Returns:
        str: testo ripulito senza punteggiatura
    """
    punctuation = ".,;:!?\"\”\‘\’«»\'\"()`-[]{}"
    for char in punctuation:
        text = text.replace(char, "")
    return text


# dizionario per raccogliere la frequenza delle parole
word_frequency = {}

# leggiamo i file
for filepath in filepaths:
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

        words = remuve_punctuaction(content).lower().strip().split()

        for word in words:
            if word not in word_frequency:
                word_frequency[word] = 1
            else:
                word_frequency[word] += 1

print(word_frequency)

# scriviamo il risultato su un file word_frequencies.txt
with open(save_frequences, 'w', encoding='utf-8') as file:
    # TRASFORMIAMO IL DIZIONARIO IN STRINGA PER POTERLO SALVARE
    for key, values in word_frequency.items():
        file.write(f"{key}: {values}\n")

print(
    f"Salvataggio avvenuto con successo nel file `{os.path.basename(save_frequences)}`")
