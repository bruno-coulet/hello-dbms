from data_processing import load_and_clean_country_data, load_and_clean_world_data
from insert_data import insert_country_data_to_db, insert_world_data_to_db
from database import create_database, create_tables, create_connection 
import logging

# Configuration des logs
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Créer la base de données et les tables si elles n'existent pas
    create_database()  # Créer la base de données si nécessaire
    create_tables()    # Créer les tables si elles n'existent pas
    
    # Connexion à la base de données
    connection = create_connection()
    if connection is None:
        logging.error("Erreur de connexion à la base de données. L'exécution est arrêtée.")
        return

    try:
        # Chemins vers les fichiers CSV
        country_file_path = './pre_processed_data/Country.csv'
        world_file_path = './pre_processed_data/World.csv'

        # Traitement et nettoyage des données pays
        country_df = load_and_clean_country_data(country_file_path)
        if country_df is not None:
            insert_country_data_to_db(country_df)  # N'envoyez pas la connexion ici
        else:
            logging.error("Erreur lors du chargement et du nettoyage des données pays.")
        
        # Traitement et nettoyage des données mondiales
        world_df = load_and_clean_world_data(world_file_path)
        if world_df is not None:
            insert_world_data_to_db(world_df)  # N'envoyez pas la connexion ici
        else:
            logging.error("Erreur lors du chargement et du nettoyage des données mondiales.")

    except Exception as e:
        logging.error(f"Erreur lors de l'exécution du programme : {e}")
    
    finally:
        # Fermeture de la connexion à la base de données
        if connection.is_connected():
            connection.close()
            logging.info("Connexion à la base de données fermée.")

if __name__ == "__main__":
    main()
