"""
Crea un programma che legga più file di testo e stampi la prima frase di ogni file di testo nel terminale.
(1) Il programma scorre i file di testo e legge il contenuto di ciascuno di essi mediante un ciclo for.
(2) Il programma estrae la prima frase di ogni file di testo, preferibilmente utilizzando la libreria re.
(3) Il programma stampa le frasi estratte nel terminale, una per riga
"""
import os
import re

# directory cartella progetto
FOLDER = os.path.dirname(os.path.abspath(__file__))
# directori alla sotto cartella
SUBFOLDER = os.path.join(FOLDER, 'resources')
# lista di tutti i file all'interno della sotto cartella...
# uso una listcomprehension per escludere i file nascosti (quelli con il .)
contents_under_folder = [f for f in os.listdir(
    SUBFOLDER) if not f.startswith(".")]
# ['antarctica.txt', 'atlantic.txt', 'indian.txt', 'pacific.txt', 'urls.txt']


# Pattern spiegato:
# (          -> Inizio gruppo di cattura
#  .+?       -> Qualsiasi carattere (non-greedy)
#  \.        -> Un punto letterale
#  (?:\s|$)  -> Seguito da uno spazio (non catturato) o fine riga
# )          -> Fine gruppo di cattura
# \s* -> Include gli spazi opzionali dopo il punto nel match

pattern = r"(.+?\.(?:\s|$))\s*"
sentences = ''
for filename in contents_under_folder:
    # percorso singolo file
    filepath = os.path.join(SUBFOLDER, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.readline()
        match = re.search(pattern, content)
        if match:
            sentences += match.group(0)


if sentences:
    print(sentences)
