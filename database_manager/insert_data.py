import mysql.connector
from mysql.connector import Error
import logging
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

# Configuration des logs
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Fonction pour insérer les données dans la table Country
def insert_country_data_to_db(df):
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    if connection:
        cursor = connection.cursor()
        try:
            for index, row in df.iterrows():
                # Vérification si le pays existe déjà dans la base de données
                cursor.execute("SELECT id FROM Country WHERE country = %s", (row['country'],))
                result = cursor.fetchone()

                if not result:  # Si le pays n'existe pas déjà
                    cursor.execute(''' 
                        INSERT INTO Country (country, coal_emissions, gas_emissions, oil_emissions, hydro_emissions, renewable_emissions, nuclear_emissions)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ''', (row['country'], row['coal_emissions'], row['gas_emissions'], row['oil_emissions'], row['hydro_emissions'], row['renewable_emissions'], row['nuclear_emissions']))
                    logging.info(f"Insertion réussie pour le pays: {row['country']}")
                else:
                    logging.info(f"Le pays {row['country']} existe déjà dans la base de données. Aucune insertion effectuée.")
            
            connection.commit()
            logging.info("Données insérées avec succès dans la table 'Country'.")
        except Error as e:
            logging.error(f"Erreur lors de l'insertion des données dans 'Country': {e}")
        finally:
            cursor.close()
            connection.close()
            logging.info("Connexion fermée après insertion des données dans 'Country'.")

# Fonction pour insérer les données dans la table World
def insert_world_data_to_db(df):
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    if connection:
        cursor = connection.cursor()
        try:
            for index, row in df.iterrows():
                # Vérification si la région existe déjà dans la base de données
                cursor.execute("SELECT id FROM World WHERE region = %s", (row['region'],))
                result = cursor.fetchone()

                if not result:  # Si la région n'existe pas déjà
                    cursor.execute(''' 
                        INSERT INTO World (region, coal_emissions_total, gas_emissions_total, oil_emissions_total, hydro_emissions_total, renewable_emissions_total, nuclear_emissions_total)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ''', (row['region'], row['coal_emissions_total'], row['gas_emissions_total'], row['oil_emissions_total'], row['hydro_emissions_total'], row['renewable_emissions_total'], row['nuclear_emissions_total']))
                    logging.info(f"Insertion réussie pour la région: {row['region']}")
                else:
                    logging.info(f"La région {row['region']} existe déjà dans la base de données. Aucune insertion effectuée.")
            
            connection.commit()
            logging.info("Données insérées avec succès dans la table 'World'.")
        except Error as e:
            logging.error(f"Erreur lors de l'insertion des données dans 'World': {e}")
        finally:
            cursor.close()
            connection.close()
            logging.info("Connexion fermée après insertion des données dans 'World'.")
