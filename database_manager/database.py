
import mysql.connector
from mysql.connector import Error
import logging
import config

# Configuration des logs
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_connection(db_name=None):
    try:
        connection = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=db_name
        )
        if connection.is_connected():
            logging.info(f"Connexion à la base de données {'réussie' if db_name else 'au serveur MySQL réussie'}")
        return connection
    except Error as e:
        logging.error(f"Erreur lors de la connexion {'à la base de données' if db_name else 'au serveur MySQL'}: {e}")
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
    connection = create_connection('carbon_footprint')
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Country (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    country VARCHAR(100),
                    coal_emissions DECIMAL(10, 2),
                    gas_emissions DECIMAL(10, 2),
                    oil_emissions DECIMAL(10, 2),
                    hydro_emissions DECIMAL(10, 2),
                    renewable_emissions DECIMAL(10, 2),
                    nuclear_emissions DECIMAL(10, 2)
                )
            ''')
            logging.info("Table 'Country' créée ou déjà existante.")

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS World (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    region VARCHAR(100),
                    coal_emissions_total DECIMAL(10, 2),
                    gas_emissions_total DECIMAL(10, 2),
                    oil_emissions_total DECIMAL(10, 2),
                    hydro_emissions_total DECIMAL(10, 2),
                    renewable_emissions_total DECIMAL(10, 2),
                    nuclear_emissions_total DECIMAL(10, 2)
                )
            ''')
            logging.info("Table 'World' créée ou déjà existante.")

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Emissions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    source VARCHAR(100),
                    min_gCO2_kWh DECIMAL(10, 2),
                    median_gCO2_kWh DECIMAL(10, 2),
                    max_gCO2_kWh DECIMAL(10, 2)
                )
            ''')
            logging.info("Table 'Emissions' créée ou déjà existante.")
        except Error as e:
            logging.error(f"Erreur lors de la création des tables: {e}")
        finally:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    create_database()
    create_tables()

