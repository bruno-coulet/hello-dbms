import pandas as pd
import logging
import csv
import re

# Configuration des logs
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_text(text):
    # Supprimer les caractères indésirables
    cleaned_text = re.sub(r'[^\x00-\x7F]+', '', text)
    if cleaned_text != text:
        logging.info(f"Caractères indésirables supprimés: {text} -> {cleaned_text}")
    return cleaned_text

def clean_text_with_accents(text):
    # Supprimer uniquement les caractères indésirables spécifiques, sans supprimer les accents
    cleaned_text = re.sub(r'[^\w\s,;]', '', text)
    if cleaned_text != text:
        logging.info(f"Caractères indésirables supprimés: {text} -> {cleaned_text}")
    return cleaned_text

def load_and_clean_country_data(file_path):
    try:
        logging.info(f"Chargement du fichier {file_path}")
        # Chargement du fichier CSV dans un DataFrame avec gestion des erreurs de tokenisation
        df = pd.read_csv(file_path, sep=';', on_bad_lines='skip', encoding='utf-8', quoting=csv.QUOTE_NONE)
        logging.info(f"Fichier {file_path} chargé avec succès.")
        
        # Vérification du nombre de colonnes dans le fichier
        if df.shape[1] != 7:
            logging.warning(f"Le fichier {file_path} n'a pas le nombre de colonnes attendu. Colonnes trouvées: {df.shape[1]}")
        
        # Suppression des lignes avec des valeurs manquantes
        df.dropna(inplace=True)
        logging.info(f"Valeurs manquantes supprimées.")

        # Nettoyage des données pour supprimer les caractères indésirables
        df = df.apply(lambda col: col.map(clean_text) if col.dtype == 'object' else col)
        logging.info(f"Caractères indésirables supprimés.")

        # Renommage des colonnes pour les rendre cohérentes
        expected_columns = ['country', 'coal_emissions', 'gas_emissions', 'oil_emissions', 'hydro_emissions', 'renewable_emissions', 'nuclear_emissions']
        if len(df.columns) == len(expected_columns):
            df.columns = expected_columns
            logging.info("Colonnes renommées avec succès.")
        else:
            logging.error(f"Erreur dans le renommage des colonnes. Le nombre de colonnes ne correspond pas à {len(expected_columns)}.")
            return None
        
        return df

    except pd.errors.ParserError as e:
        logging.error(f"Erreur de parsing CSV dans le fichier {file_path}: {e}")
        return None
    except Exception as e:
        logging.error(f"Erreur lors du traitement des données pays: {e}")
        return None

def load_and_clean_world_data(file_path):
    try:
        logging.info(f"Chargement du fichier {file_path}")
        # Chargement du fichier CSV dans un DataFrame avec gestion des erreurs de tokenisation
        df = pd.read_csv(file_path, sep=';', on_bad_lines='skip', encoding='utf-8', quoting=csv.QUOTE_NONE)
        logging.info(f"Fichier {file_path} chargé avec succès.")
        
        # Vérification du nombre de colonnes dans le fichier
        if df.shape[1] != 7:
            logging.warning(f"Le fichier {file_path} n'a pas le nombre de colonnes attendu. Colonnes trouvées: {df.shape[1]}")
        
        # Suppression des lignes avec des valeurs manquantes
        df.dropna(inplace=True)
        logging.info(f"Valeurs manquantes supprimées.")

        # Nettoyage des données pour supprimer les caractères indésirables
        df = df.apply(lambda col: col.map(clean_text) if col.dtype == 'object' else col)
        logging.info(f"Caractères indésirables supprimés.")

        # Renommage des colonnes pour les rendre cohérentes
        expected_columns = ['region', 'coal_emissions_total', 'gas_emissions_total', 'oil_emissions_total', 'hydro_emissions_total', 'renewable_emissions_total', 'nuclear_emissions_total']
        if len(df.columns) == len(expected_columns):
            df.columns = expected_columns
            logging.info("Colonnes renommées avec succès.")
        else:
            logging.error(f"Erreur dans le renommage des colonnes. Le nombre de colonnes ne correspond pas à {len(expected_columns)}.")
            return None
        
        return df

    except pd.errors.ParserError as e:
        logging.error(f"Erreur de parsing CSV dans le fichier {file_path}: {e}")
        return None
    except Exception as e:
        logging.error(f"Erreur lors du traitement des données mondiales: {e}")
        return None

def load_and_clean_emission_data(file_path):
    try:
        logging.info(f"Chargement du fichier {file_path}")
        # Chargement du fichier CSV dans un DataFrame avec gestion des erreurs de tokenisation
        df = pd.read_csv(file_path, sep=';', on_bad_lines='skip', encoding='utf-8', quoting=csv.QUOTE_NONE)
        logging.info(f"Fichier {file_path} chargé avec succès.")
        
        # Suppression des lignes avec des valeurs manquantes
        df.dropna(inplace=True)
        logging.info(f"Valeurs manquantes supprimées.")

        # Nettoyage des données pour supprimer les caractères indésirables
        df = df.apply(lambda col: col.map(clean_text_with_accents) if col.dtype == 'object' else col)
        logging.info(f"Caractères indésirables supprimés.")

        # Renommage des colonnes pour les rendre cohérentes
        expected_columns = ['Source', 'Min de gCO2/kWh', 'Médiane de gCO2/kWh', 'Max de gCO2/kWh']
        if len(df.columns) == len(expected_columns):
            df.columns = expected_columns
            logging.info("Colonnes renommées avec succès.")
        else:
            logging.error(f"Erreur dans le renommage des colonnes. Le nombre de colonnes ne correspond pas à {len(expected_columns)}.")
            return None
        
        return df

    except pd.errors.ParserError as e:
        logging.error(f"Erreur de parsing CSV dans le fichier {file_path}: {e}")
        return None
    except Exception as e:
        logging.error(f"Erreur lors du traitement des données d'émissions: {e}")
        return None
