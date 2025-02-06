import os
import pandas as pd
from openpyxl import load_workbook

directory_path = "/home/rh/dev/automation_training/dataExtractor/excel test"
result_file = "result.xlsx"

extract_cells = ["A1"]

data = []

for file_name in os.listdir(directory_path):
    if file_name.endswith(".xlsx") and not file_name.startswith("~$"):
        file_path = os.path.join(directory_path, file_name)
        try:
            wb = load_workbook(file_path, data_only=True)
            sheet = wb.active

            values = [file_name]
            for cell in extract_cells:
                value = sheet[cell].value
                values.append(value)

            data.append(values)

        except Exception as e:
            print(f"Erreur avec {file_name}: {e}")

columns = ["File"] + extract_cells
df = pd.DataFrame(data, columns=columns)

df.to_excel(result_file, index=False)

print(f"Extraction terminée. Résultats enregistrés dans '{result_file}'.")
