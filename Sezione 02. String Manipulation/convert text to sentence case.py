# Crea un programma che legga il testo di un file di testo, lo converta in "Sentence case"
# e salvi il risultato in un nuovo file di testo.
# Il programma dovrebbe rendere maiuscola la prima lettera di ogni frase e salvare il risultato in un nuovo file snowwhite_corrected.txt.
import os

# percorso principale
script_dir = os.path.dirname(os.path.abspath(__file__))
# percorso file target input per la lettura e target output per la scrittura
target_file_input = os.path.join(script_dir, "snowwhite.txt")
target_file_output = os.path.join(script_dir, "snowwhite_corrected.txt")

with open(target_file_input) as file:
    text = file.read()  # legge tutto il file e crea una stringa

# splitto al punto(. )
sentence = text.split(". ")

# trasformo la prima lettera di ogni frase in maiuscola
correct_sentence = [x.capitalize() for x in sentence]

# aggiungo il . a fine frase e unisco in una sola stringa
testo_corretto = ". ".join(correct_sentence)

# provvedo alla scrittura del file `snowwhite_corrected.txt` con il testo_corretto
with open(target_file_output, "w") as file:
    file.write(testo_corretto)
