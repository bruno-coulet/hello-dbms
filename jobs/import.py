import pandas as pd
import pymysql
import os
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

# Charger les données CSV dans un DataFrame Pandas
df = pd.read_csv(DATA)

# Afficher les premières lignes du DataFrame avant nettoyage
print("Affichage des premières lignes du DataFrame avant nettoyage des valeurs :")
print(df.head())

# Nettoyage des données pour les autres colonnes (exclure 'Country' et 'Region')
def clean_value(val):
    """Nettoyer les valeurs avant insertion dans la base de données"""
    if isinstance(val, str):
        val = val.strip()  # Supprimer les espaces en début et fin de chaîne
        val = val.replace(',', '.')  # Remplacer la virgule par un point
    try:
        return float(val) if val not in ["", "N/A", "NaN"] else None
    except ValueError:
        return None  # Retourner None si la conversion échoue

# Appliquer le nettoyage sur chaque colonne sauf 'Country' et 'Region'
columns_to_clean = [col for col in df.columns if col not in ['Country', 'Region']]
df[columns_to_clean] = df[columns_to_clean].applymap(clean_value)

# Affichage des premières lignes du DataFrame après nettoyage
print("\nAffichage des premières lignes du DataFrame après nettoyage des autres colonnes :")
print(df[['Country', 'Region'] + columns_to_clean].head())

# Connexion à la base de données avec pymysql
con = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = con.cursor()

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

# Générer les colonnes SQL avec les types appropriés, en échappant les noms des colonnes
colonnes = ", ".join([f"`{col}` {type_mapping.get(col, 'VARCHAR(255)')}" for col in df.columns])

# Créer la table
creation_table = f"CREATE TABLE IF NOT EXISTS {nom_table} ({colonnes});"
cursor.execute(creation_table)

# Créer le dossier de logs si il n'existe pas
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Fichier log
log_file = os.path.join(log_dir, 'logs.json')

# Ouvrir le fichier log en mode écriture (le fichier sera écrasé à chaque lancement)
with open(log_file, 'w') as log:
    # Insertion des données
    for index, ligne in df.iterrows():
        valeurs = []

        # Log de la ligne avant insertion
        log.write(f"Insertion dans la base de données : Country = {ligne['Country']}, Region = {ligne['Region']}, {', '.join([str(v) for v in ligne[2:].values])}\n")

        for col, val in ligne.items():
            if pd.isna(val):  # Si la valeur est NaN (manquante)
                valeurs.append('NULL')
            elif isinstance(val, str):  # Si la valeur est une chaîne de caractères
                valeurs.append(f"'{val}'")
            else:  # Pour les valeurs numériques (float, int)
                valeurs.append(str(val))  # Convertir en chaîne sans guillemets

        # Créer l'instruction SQL d'insertion
        insertion = f"INSERT INTO {nom_table} ({', '.join([f'`{col}`' for col in df.columns])}) VALUES ({', '.join(valeurs)});"

        # Exécuter l'insertion
        cursor.execute(insertion)

    # Valider les changements et fermer la connexion
    con.commit()

cursor.close()
con.close()

print("\nLes données ont été insérées avec succès.")
