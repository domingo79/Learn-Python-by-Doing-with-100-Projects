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
# escludo file non necessari al progetto
files_name = [name for name in os.listdir(RESOURCES) if not (
    name.startswith(".") or name.startswith("email_"))]
# creo le directory dei file
file_paths = [os.path.join(RESOURCES, dir_file) for dir_file in files_name]

# leggiamo e aggreghiamo i dati in un dataframe per anno
data_frame_2024 = [pd.read_excel(
    file_path) for file_path in file_paths if file_path.endswith('2024.xlsx')]
data_frame_2025 = [pd.read_excel(
    file_path) for file_path in file_paths if file_path.endswith('2025.xlsx')]

# # concateniamo i file per anno
merged_df_2024 = pd.concat(data_frame_2024)
merged_df_2025 = pd.concat(data_frame_2025)

# # gestisco le cartelle di export
OUTPUT = os.path.join(FOLDER, 'output')
filename_merged_2024 = "2024.xlsx"
filename_merged_2025 = "2025.xlsx"
output_filepath_2024 = os.path.join(OUTPUT, filename_merged_2024)
output_filepath_2025 = os.path.join(OUTPUT, filename_merged_2025)

# # esportiamo i file
merged_df_2024.to_excel(output_filepath_2024, index=False)
merged_df_2025.to_excel(output_filepath_2025, index=False)
