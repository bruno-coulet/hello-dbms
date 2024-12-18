import pandas as pd
import pymysql
import os
import json
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration de la base de données
db_host = os.getenv('DB_HOST', 'localhost')
db_user = os.getenv('USER')
db_password = os.getenv('PASSWORD')
db_name = os.getenv('DATABASE')

# Chemin vers les données CSV (ajusté pour le sous-dossier 'jobs')
DATA = "./raw_data/countries.csv"

# Créer le dossier de logs si il n'existe pas
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Fichier log
log_file = os.path.join(log_dir, 'logs.json')

# Initialiser les logs
logs = {
    "steps": [],
    "errors": []
}

def log_step(category, message, success=True):
    """Ajouter une étape aux logs"""
    logs["steps"].append({
        "category": category,
        "message": message,
        "success": success
    })

def log_error(category, message):
    """Ajouter une erreur aux logs"""
    logs["errors"].append({
        "category": category,
        "message": message
    })

# Charger les données CSV
try:
    df = pd.read_csv(DATA)
    log_step("Data Loading", f"Loaded data from {DATA}.", success=True)
except Exception as e:
    log_error("Data Loading", f"Failed to load data: {str(e)}")
    with open(log_file, 'w') as log:
        json.dump(logs, log, indent=4)
    raise e

# Nettoyage des données
def clean_value(val):
    """Nettoyer les valeurs avant insertion dans la base de données"""
    if isinstance(val, str):
        val = val.strip()  # Supprimer les espaces en début et fin de chaîne
        val = val.replace(',', '.')  # Remplacer la virgule par un point
    try:
        return float(val) if val not in ["", "N/A", "NaN"] else None
    except ValueError:
        return None  # Retourner None si la conversion échoue

try:
    # Nettoyage des colonnes 'Country' et 'Region'
    df['Country'] = df['Country'].str.strip().apply(lambda x: x.replace("'", "''"))
    df['Region'] = df['Region'].str.strip().apply(lambda x: x.replace("'", "''"))

    # Nettoyage des autres colonnes
    columns_to_clean = [col for col in df.columns if col not in ['Country', 'Region']]
    df[columns_to_clean] = df[columns_to_clean].applymap(clean_value)

    log_step("Data Cleaning", "Data cleaning completed successfully.", success=True)
except Exception as e:
    log_error("Data Cleaning", f"Error during data cleaning: {str(e)}")
    with open(log_file, 'w') as log:
        json.dump(logs, log, indent=4)
    raise e

# Connexion à la base de données
try:
    con = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = con.cursor()
    log_step("SQL Connection", "Connected to the database successfully.", success=True)
except Exception as e:
    log_error("SQL Connection", f"Failed to connect to the database: {str(e)}")
    with open(log_file, 'w') as log:
        json.dump(logs, log, indent=4)
    raise e

# Création de la table
nom_table = 'countries'
type_mapping = {
    "Country": "VARCHAR(255)",
    "Region": "VARCHAR(255)",
    "Population": "INT",
    "Area_sq_mi": "FLOAT",
    "Pop_Density_per_sq_mi": "FLOAT",
    "Coastline_coast/area_ratio": "FLOAT",
    "Net_migration": "FLOAT",
    "Infant_mortality_per_1000_births": "FLOAT",
    "GDP_$_per_capita": "INT",
    "Literacy_%": "FLOAT",
    "Phones_per_1000": "FLOAT",
    "Arable_%": "FLOAT",
    "Crops_%": "FLOAT",
    "Other_%": "FLOAT",
    "Climate": "INT",
    "Birthrate": "FLOAT",
    "Deathrate": "FLOAT",
    "Agriculture": "FLOAT",
    "Industry": "FLOAT",
    "Service": "FLOAT",
}

try:
    colonnes = ", ".join([f"`{col}` {type_mapping.get(col, 'VARCHAR(255)')}" for col in df.columns])
    creation_table = f"CREATE TABLE IF NOT EXISTS {nom_table} ({colonnes});"
    cursor.execute(creation_table)
    log_step("SQL Table Creation", f"Table '{nom_table}' created or verified successfully.", success=True)
except Exception as e:
    log_error("SQL Table Creation", f"Failed to create the table: {str(e)}")
    with open(log_file, 'w') as log:
        json.dump(logs, log, indent=4)
    raise e

# Insertion des données
try:
    for index, ligne in df.iterrows():
        valeurs = []
        for col, val in ligne.items():
            if pd.isna(val):  # Si la valeur est NaN (manquante)
                valeurs.append('NULL')
            elif isinstance(val, str):  # Si la valeur est une chaîne de caractères
                valeurs.append(f"'{val}'")
            else:  # Pour les valeurs numériques (float, int)
                valeurs.append(str(val))

        insertion = f"INSERT INTO {nom_table} ({', '.join([f'`{col}`' for col in df.columns])}) VALUES ({', '.join(valeurs)});"
        cursor.execute(insertion)
    con.commit()
    log_step("Data Insertion", "Data inserted successfully into the database.", success=True)
except Exception as e:
    log_error("Data Insertion", f"Error during data insertion: {str(e)}")
    with open(log_file, 'w') as log:
        json.dump(logs, log, indent=4)
    raise e

# Fermeture de la connexion
cursor.close()
con.close()

# Enregistrement des logs
with open(log_file, 'w') as log:
    json.dump(logs, log, indent=4)
