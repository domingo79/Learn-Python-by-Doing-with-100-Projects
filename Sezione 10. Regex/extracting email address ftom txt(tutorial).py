import os
import re

# percorso relativo
directory = 'Sezione 10. Regex/documents'

# otteniamo tutti i file allinterno di directory
filenames = os.listdir(directory)

pattern_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}"
all_email = []

for filename in filenames:
    # ricostruiamo l'intero percorso del file per darlo in pasto ad open()
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        content = f.read()

        # costruiamo lo schema per trovare le email
        # supporto_it@helpdesk-cloud.com.
        email_trovate = re.findall(pattern_email, content)
        # uso extend() per avere una lista di email non una lista di liste come farebbe append()
        all_email.extend(email_trovate)

if all_email:
    print(f"Email travate {len(all_email)}: \n{all_email}")
