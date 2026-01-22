"""
Dobbiamo creare uno script che esamina una cartella "resources" che contiene dei file excel e mergiare
gli stessi file in base agli anni 2024 e 2025 e una volta mergiati i file in base agli anni corretti
creamo i file "2024.xlsx" e "2025.xlsx" nella cartella "output"
"""
import os
import pandas as pd

# gestiamo le cartelle
FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCES = os.path.join(FOLDER, 'resources')
OUTPUT = os.path.join(FOLDER, 'output')
# escludo file non necessari al progetto
file_paths = [os.path.join(RESOURCES, dir_file) for dir_file in os.listdir(
    RESOURCES) if not (dir_file.startswith(".") or dir_file.startswith("email_"))]


def merge_by_year(file_paths, year: str) -> pd.DataFrame:
    dfs = [pd.read_excel(path)
           for path in file_paths if path.endswith(f"{year}.xlsx")]
    return pd.concat(dfs, ignore_index=True)


for year in ("2024", "2025"):
    merged = merge_by_year(file_paths, year)
    merged.to_excel(os.path.join(OUTPUT, f"{year}.xlsx"), index=False)
    print(f"Merged data for {year} saved to '..\\output\\{year}.xlsx'.")
