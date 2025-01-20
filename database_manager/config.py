import os
from dotenv import load_dotenv
import logging

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Variables de configuration pour la base de données et les logs
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
LOG_DIR = os.getenv("LOG_DIR", "/default/log/path")
LOG_FILE = os.getenv("LOG_FILE", "app.log") 

# Vérification que les variables de la base de données sont présentes
if not all([DB_HOST, DB_USER, DB_PASSWORD, DB_NAME]):
    logging.error("Les variables d'environnement pour la base de données sont manquantes.")
    raise ValueError("Les variables d'environnement nécessaires pour la base de données sont manquantes.")
