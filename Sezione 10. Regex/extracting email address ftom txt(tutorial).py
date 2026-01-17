import os
import re

# Percorso alla cartella dove si trova lo script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Percorso locale alla sezione
resources_dir = os.path.join(script_dir, "resources")

# otteniamo tutti i file allinterno di resources
filenames = os.listdir(resources_dir)

pattern_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}"
all_email = []

for filename in filenames:
    # ricostruiamo l'intero percorso del file per darlo in pasto ad open()
    filepath = os.path.join(resources_dir, filename)
    with open(filepath, "r") as f:
        content = f.read()

        # costruiamo lo schema per trovare le email
        # supporto_it@helpdesk-cloud.com.
        email_trovate = re.findall(pattern_email, content)
        # uso extend() per avere una lista di email non una lista di liste come farebbe append()
        all_email.extend(email_trovate)

if all_email:
    print(f"Email travate {len(all_email)}: \n{all_email}")