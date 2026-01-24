import pandas
import os

FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCES = os.path.join(FOLDER, 'resources')
OUTPUT = os.path.join(FOLDER, 'output')
data_entri = os.path.join(RESOURCES, "europe.xlsx")
save_data = os.path.join(OUTPUT, "europe.json")


def convert_excel_to_JSON(excel_file):
    # legge excel
    df = pandas.read_excel(excel_file)
    # salva in JSON
    json_data = df.to_json(orient='records')
    return json_data
