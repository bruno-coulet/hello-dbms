# database_handler.py
import pymysql
from config import db_host, db_user, db_password, db_name
import pandas as pd
import time  # Pour mesurer le temps d'exécution
from data_cleaner import DataCleaner  # Importer le DataCleaner

class DatabaseHandler:
    @staticmethod
    def create_connection():
        try:
            con = pymysql.connect(
                host=db_host,
                user=db_user,
                password=db_password,
                database=db_name
            )
            return con
        except Exception as e:
            raise Exception(f"Failed to connect to the database: {str(e)}")

    @staticmethod
    def table_exists(cursor, table_name):
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        result = cursor.fetchone()
        return result is not None

    @staticmethod
    def get_table_description(cursor, table_name):
        """Récupérer la description de la table (colonnes et types) sous forme de dictionnaire."""
        cursor.execute(f"DESCRIBE {table_name}")
        columns_info = cursor.fetchall()
        columns_description = []
        for column in columns_info:
            column_name = column[0]
            column_type = column[1]
            columns_description.append({
                "column_name": column_name,
                "data_type": column_type
            })
        return columns_description

    @staticmethod
    def create_table(cursor, df, table_name='countries', logger=None):
        if DatabaseHandler.table_exists(cursor, table_name):
            if logger:
                logger.log_step("Table Creation", f"Table '{table_name}' already exists. No need to create.", success=True)
            return False  # La table existe déjà

        # Ajouter "Country" comme clé primaire
        type_mapping = {
            "Country": "VARCHAR(255) PRIMARY KEY", 
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

        # Créer la requête SQL pour créer la table
        colonnes = ", ".join([f"`{col}` {type_mapping.get(col, 'VARCHAR(255)')}" for col in df.columns])
        creation_table = f"CREATE TABLE IF NOT EXISTS {table_name} ({colonnes});"

        start_time = time.time()  # Mesurer le temps de création de la table
        cursor.execute(creation_table)
        end_time = time.time()

        # Récupérer la description de la table sous forme structurée
        table_description = DatabaseHandler.get_table_description(cursor, table_name)

        # Log des détails de la création de la table avec structure détaillée
        if logger:
            formatted_table_description = [
                {
                    "column_name": col["column_name"].replace(" ", "_"),  # Remplacer les espaces par des underscores
                    "data_type": type_mapping.get(col["column_name"], "VARCHAR(255)")
                }
                for col in table_description
            ]
            logger.log_step("Table Creation", {
                "table_name": table_name,
                "creation_time_seconds": round(end_time - start_time, 2),
                "table_structure": formatted_table_description
            }, success=True)

        return True  # La table a été créée

    @staticmethod
    def insert_data(cursor, df, table_name='countries', logger=None):
        rows_inserted = 0
        rows_ignored = 0  # Compteur pour les lignes ignorées
        start_time = time.time()  # Mesurer le temps d'insertion des données

        # Nettoyer les données avant l'insertion
        df = DataCleaner.clean_data(df)

        for index, ligne in df.iterrows():
            # Si "Country" est une clé primaire, une ligne existante provoque une erreur lors de l'insertion,
            # mais vous pouvez ignorer l'erreur avec "INSERT IGNORE" pour ne pas insérer les doublons.
            valeurs = []
            for col, val in ligne.items():
                if pd.isna(val):
                    valeurs.append('NULL')
                elif isinstance(val, str):
                    valeurs.append(f"'{val}'")
                else:
                    valeurs.append(str(val))

            insertion = f"INSERT IGNORE INTO {table_name} ({', '.join([f'`{col}`' for col in df.columns])}) VALUES ({', '.join(valeurs)});"
            cursor.execute(insertion)
            
            # Vérifier si l'insertion a eu lieu
            if cursor.rowcount > 0:  # Si une ligne a été insérée
                rows_inserted += 1
            else:  # Si la ligne a été ignorée
                rows_ignored += 1
        
        end_time = time.time()  # Mesurer la fin de l'insertion des données

        # Log des résultats
        if logger:
            logger.log_step("Data Insertion", 
                             f"{rows_inserted} rows inserted and {rows_ignored} rows ignored into '{table_name}' in {end_time - start_time:.2f} seconds.", 
                             success=True)
        return rows_inserted, rows_ignored  # Retourner le nombre de lignes insérées et ignorées
