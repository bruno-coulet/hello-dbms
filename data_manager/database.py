
import mysql.connector
from mysql.connector import Error
import logging
import config

# Configuration des logs
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,  # Remplace par ton mot de passe
            database=config.DB_NAME
        )
        if connection.is_connected():
            logging.info("Connexion à la base de données réussie")
        return connection
    except Error as e:
        logging.error(f"Erreur lors de la connexion à la base de données: {e}")
        return None

def create_database():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS carbon_footprint")
            logging.info("Base de données 'carbon_footprint' créée ou déjà existante.")
        except Error as e:
            logging.error(f"Erreur lors de la création de la base de données: {e}")
        finally:
            cursor.close()
            connection.close()

def create_tables():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Country (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    country VARCHAR(100),
                    coal_emissions FLOAT,
                    gas_emissions FLOAT,
                    oil_emissions FLOAT,
                    hydro_emissions FLOAT,
                    renewable_emissions FLOAT,
                    nuclear_emissions FLOAT
                )
            ''')
            logging.info("Table 'Country' créée ou déjà existante.")

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS World (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    region VARCHAR(100),
                    coal_emissions_total FLOAT,
                    gas_emissions_total FLOAT,
                    oil_emissions_total FLOAT,
                    hydro_emissions_total FLOAT,
                    renewable_emissions_total FLOAT,
                    nuclear_emissions_total FLOAT
                )
            ''')
            logging.info("Table 'World' créée ou déjà existante.")
        except Error as e:
            logging.error(f"Erreur lors de la création des tables: {e}")
        finally:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
    create_tables()
