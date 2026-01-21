"""
Crea un programma che carica un file di database, interroga alcune righe in base a una condizione e stampa le righe nel terminale.
(1) Il programma carica il file data.db.
(2) Interroga la tabella invoices ottenendo tutte le righe in cui BillingCountry è Germany
e la colonna Totale ha un valore pari o superiore a 2.0.
Sfida facoltativa: invece di stampare tutte le righe che soddisfano la condizione, stampare solo i valori CustomerId.
"""
import os
import sqlite3

script_dir = os.path.dirname(os.path.abspath(__file__))
resource_data = os.path.join(script_dir, r'resources\data.db')

connessione = sqlite3.connect(resource_data)
cursore = connessione.cursor()

query = """
SELECT * FROM invoices
WHERE BillingCountry = 'Germany' AND total >= 2.0
"""

cursore.execute(query)
rows = cursore.fetchall()

for row in rows:
    print(row)

connessione.close()
