"""scaletta :
    1. importare sqlite3
    2. definire la directory al db
    3. creare la connessione
    4. creare il cursore
    5. crare la query
    6. eseguire la query
    7. catturare i risultati
    8. stampare i risultati
    9. chiudere la connessione"""
import sqlite3  # 1.
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
resource_data = os.path.join(
    script_dir, r'resources\data.db')  # 2.

conn = sqlite3.connect(resource_data)  # 3.
cursore = conn.cursor()  # 4.

query = """
SELECT * FROM albums
WHERE Title LIKE '%Live%' AND LENGTH(Title) > 10
"""  # 5.

cursore.execute(query)  # 6.
rows = cursore.fetchall()  # 7.

for row in rows:  # 8.
    print(f"{row[0]:>3}: {row[1]}")

conn.close()  # 9.
