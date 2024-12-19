import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration de la base de données
db_host = os.getenv('DB_HOST', 'localhost')
db_user = os.getenv('USER')
db_password = os.getenv('PASSWORD')
db_name = os.getenv('DATABASE')

# Chemin relatif vers le fichier CSV depuis le dossier src
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../raw_data/countries.csv')

# Chemin vers le fichier de log
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
log_file = os.path.join(log_dir, 'logs.json')
