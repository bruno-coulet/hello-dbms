from database_handler import DatabaseHandler
from data_cleaner import DataCleaner
from logger import Logger
from config import *
import pandas as pd
import time

def main():
    # Initialiser les logs
    logger = Logger(log_file)

    try:
        # Étape 1 : Charger les données depuis le fichier CSV
        start_time = time.time()
        df = pd.read_csv(DATA)
        end_time = time.time()
        logger.log_step("Data Loading", f"Loaded data from {DATA} in {end_time - start_time:.2f} seconds.", success=True)

        # Étape 2 : Nettoyer les données (au niveau de DataFrame)
        start_time = time.time()
        df = DataCleaner.clean_data(df)
        end_time = time.time()
        logger.log_step("Data Cleaning", f"Data cleaning completed in {end_time - start_time:.2f} seconds.", success=True)

        # Étape 3 : Connexion à la base de données
        start_time = time.time()
        con = DatabaseHandler.create_connection()  # Connexion à la base de données
        cursor = con.cursor()
        end_time = time.time()
        logger.log_step("Database Connection", f"Connected to the database in {end_time - start_time:.2f} seconds.", success=True)

        # Étape 4 : Vérifier si la table existe ou la créer
        start_time = time.time()
        table_created = DatabaseHandler.create_table(cursor, df, logger=logger)
        end_time = time.time()

        if table_created:
            creation_time = end_time - start_time
            logger.log_step("Table Creation", f"Table created in {creation_time:.2f} seconds.", success=True)

        # Étape 5 : Insérer les données
        start_time = time.time()
        rows_inserted, rows_ignored = DatabaseHandler.insert_data(cursor, df, logger=logger)
        con.commit()
        end_time = time.time()
        logger.log_step(
            "Data Insertion",
            f"Inserted {rows_inserted} rows, ignored {rows_ignored} rows in {end_time - start_time:.2f} seconds.",
            success=True
        )

        # Étape 6 : Nettoyer les colonnes de la table dans la base de données
        start_time = time.time()
        DataCleaner.clean_table_columns(cursor, "countries", logger=logger)
        con.commit()
        end_time = time.time()
        logger.log_step(
            "Table Alteration",
            f"Table columns cleaned and modified in {end_time - start_time:.2f} seconds.",
            success=True
        )

    except Exception as e:
        # Gestion des erreurs
        logger.log_error("Main Execution", f"An error occurred: {str(e)}")
        if 'con' in locals():
            con.rollback()  # Annuler les modifications en cas d'erreur
        raise e

    finally:
        # Fermeture des ressources
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()
        # Enregistrer les logs
        logger.save_logs()

if __name__ == "__main__":
    main()
