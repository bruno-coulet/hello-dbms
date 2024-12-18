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
        # Mesurer le temps de chargement des données
        start_time = time.time()
        df = pd.read_csv(DATA)
        end_time = time.time()
        logger.log_step("Data Loading", f"Loaded data from {DATA} in {end_time - start_time:.2f} seconds.", success=True)

        # Mesurer le temps de nettoyage des données
        start_time = time.time()
        df = DataCleaner.clean_data(df)
        end_time = time.time()
        logger.log_step("Data Cleaning", f"Data cleaning completed in {end_time - start_time:.2f} seconds.", success=True)

        # Connexion à la base de données et mesure du temps
        start_time = time.time()
        con = DatabaseHandler.create_connection()  # Connexion à la base de données
        cursor = con.cursor()
        end_time = time.time()
        logger.log_step("Database Connection", f"Connected to the database in {end_time - start_time:.2f} seconds.", success=True)

        # Vérifier si la table existe déjà et la créer si nécessaire
        start_time = time.time()
        table_created = DatabaseHandler.create_table(cursor, df, logger=logger)
        end_time = time.time()

        if table_created:
            creation_time = end_time - start_time
            logger.log_step("Table Creation", f"Table created in {creation_time:.2f} seconds.", success=True)

        # Insérer les données et obtenir le nombre de lignes insérées et ignorées
        start_time = time.time()
        rows_inserted, rows_ignored = DatabaseHandler.insert_data(cursor, df, logger=logger)
        con.commit()
        end_time = time.time()



    except Exception as e:
        logger.log_error("Data Insertion", f"Error during data insertion: {str(e)}")
        raise e

    # Enregistrer les logs dans le fichier
    logger.save_logs()

if __name__ == "__main__":
    main()
