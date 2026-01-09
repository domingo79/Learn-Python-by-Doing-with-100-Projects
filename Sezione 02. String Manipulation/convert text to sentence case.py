# Crea un programma che legga il testo di un file di testo, lo converta in "Sentence case"
# e salvi il risultato in un nuovo file di testo.
# Il programma dovrebbe rendere maiuscola la prima lettera di ogni frase e salvare il risultato in un nuovo file snowwhite_corrected.txt.
import os

# percorso principale
script_dir = os.path.dirname(os.path.abspath(__file__))
# percorso file target
target_file = os.path.join(script_dir, "snowwhite.txt")

with open(target_file) as file:
    text = file.read()  # legge tutto il file e crea una stringa

words = text.split(" ")
reversed_words = [x[::-1] for x in words]
print(reversed_words)
