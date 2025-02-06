import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import tempfile

# Interface Streamlit
st.title("🗂️ Extraction de données Excel")

# Sélection de fichiers (multi-upload)
uploaded_files = st.file_uploader("Sélectionnez un ou plusieurs fichiers Excel", type=["xlsx"], accept_multiple_files=True)

# Champ pour les cellules à extraire
extract_cells = st.text_input("Entrez les cellules à extraire (ex: A1, B2, C3)", "A1")
extract_cells = [cell.strip().upper() for cell in extract_cells.split(",")]

# Vérification et extraction
if uploaded_files:
    data = []

    for uploaded_file in uploaded_files:
        try:
            # Charger le fichier Excel
            wb = load_workbook(uploaded_file, data_only=True)
            sheet = wb.active

            # Récupérer les valeurs des cellules demandées
            values = [uploaded_file.name]
            for cell in extract_cells:
                values.append(sheet[cell].value)

            data.append(values)

        except Exception as e:
            st.error(f"Erreur avec {uploaded_file.name}: {e}")

    # Création du DataFrame
    columns = ["Fichier"] + extract_cells
    df = pd.DataFrame(data, columns=columns)

    # Affichage des résultats
    st.success("Extraction terminée ! ✅")
    st.dataframe(df)

    # Sauvegarde dans un fichier temporaire pour téléchargement
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp_file:
        df.to_excel(tmp_file.name, index=False)
        st.download_button(
            label="📥 Télécharger le fichier Excel",
            data=open(tmp_file.name, "rb").read(),
            file_name="result.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
