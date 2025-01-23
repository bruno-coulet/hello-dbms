from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error
import pandas as pd
import logging
import config

# Configuration des logs
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Flask app
app = Flask(__name__)

# Database configuration
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,  
            database=config.DB_NAME
        )
        if connection.is_connected():
            logging.info("Connexion à la base de données réussie")
        return connection
    except Error as e:
        logging.error(f"Erreur lors de la connexion à la base de données: {e}")
        return None

@app.route('/')
def index():
    connection = create_connection()
    if connection is None:
        return "Erreur de connexion à la base de données", 500
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT country, coal_emissions, gas_emissions, oil_emissions, hydro_emissions, renewable_emissions, nuclear_emissions FROM country LIMIT 10;")
            country_results = cursor.fetchall()
            cursor.execute("SELECT region, coal_emissions_total, gas_emissions_total, oil_emissions_total, hydro_emissions_total, renewable_emissions_total, nuclear_emissions_total FROM world LIMIT 10;")
            world_results = cursor.fetchall()
            cursor.execute("SELECT source, min_gCO2_kWh, median_gCO2_kWh, max_gCO2_kWh FROM emissions LIMIT 10;")
            emissions_results = cursor.fetchall()
    except Error as e:
        logging.error(f"Erreur lors de l'exécution de la requête: {e}")
        return "Erreur lors de l'exécution de la requête: {e}", 500
    finally:
        connection.close()
    
    # Créer les DataFrames sans la colonne id pour country wolrd et emissions
    country_columns = ['country', 'coal_emissions', 'gas_emissions', 'oil_emissions', 'hydro_emissions', 'renewable_emissions', 'nuclear_emissions']
    world_columns = ['region', 'coal_emissions_total', 'gas_emissions_total', 'oil_emissions_total', 'hydro_emissions_total', 'renewable_emissions_total', 'nuclear_emissions_total']
    emissions_columns = ['source', 'min_gCO2_kWh', 'median_gCO2_kWh', 'max_gCO2_kWh']
    
    country_data = pd.DataFrame(country_results, columns=country_columns)
    world_data = pd.DataFrame(world_results, columns=world_columns)
    emissions_data = pd.DataFrame(emissions_results, columns=emissions_columns)
    
    return render_template('index.html', country_data=country_data.to_dict(orient='list'), world_data=world_data.to_dict(orient='list'), emissions_data=emissions_data.to_dict(orient='list'))


@app.route('/data-preview')
def data_preview():
    connection = create_connection()
    if connection is None:
        return "Erreur de connexion à la base de données", 500
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM country LIMIT 10;")
            country_results = cursor.fetchall()
            cursor.execute("SELECT * FROM world LIMIT 10;")
            world_results = cursor.fetchall()
    except Error as e:
        logging.error(f"Erreur lors de l'exécution de la requête: {e}")
        return "Erreur lors de l'exécution de la requête: {e}", 500
    finally:
        connection.close()
    
    country_data = pd.DataFrame(country_results, columns=['country', 'coal_emissions', 'gas_emissions', 'oil_emissions', 'hydro_emissions', 'renewable_emissions', 'nuclear_emissions'])
    world_data = pd.DataFrame(world_results, columns=['region', 'coal_emissions_total', 'gas_emissions_total', 'oil_emissions_total', 'hydro_emissions_total', 'renewable_emissions_total', 'nuclear_emissions_total'])
    
    return render_template('data_preview.html', country_data=country_data.to_dict(orient='list'), world_data=world_data.to_dict(orient='list'))



@app.route('/countries')
def get_countries():
    connection = create_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT country FROM country;")
        countries = [row[0] for row in cursor.fetchall()]
    connection.close()
    return countries

@app.route('/country-energy-usage')
def energy_usage():
    energy_source = request.args.get('source', 'coal_emissions')
    connection = create_connection()
    with connection.cursor() as cursor:
        query = f"""
        SELECT country, coal_emissions, gas_emissions, oil_emissions, hydro_emissions, renewable_emissions, nuclear_emissions
        FROM country
        ORDER BY {energy_source} DESC;
        """
        cursor.execute(query)
        results = cursor.fetchall()
    connection.close()
    data = pd.DataFrame(results, columns=['country', 'coal_emissions', 'gas_emissions', 'oil_emissions', 'hydro_emissions', 'renewable_emissions', 'nuclear_emissions'])
    return render_template('country_energy_usage.html', data=data.to_dict(orient='list'), energy_source=energy_source)

@app.route('/regions-energy-usage')
def regions_energy_usage():
    energy_source = request.args.get('source', 'coal_emissions_total')
    connection = create_connection()
    if connection is None:
        return "Erreur de connexion à la base de données", 500
    try:
        with connection.cursor() as cursor:
            query = f"""
            SELECT region, coal_emissions_total, gas_emissions_total, oil_emissions_total, hydro_emissions_total, renewable_emissions_total, nuclear_emissions_total
            FROM world
            ORDER BY {energy_source} DESC;
            """
            logging.info(f"Exécution de la requête : {query}")
            cursor.execute(query)
            results = cursor.fetchall()
            logging.info(f"Résultats de la requête : {results}")
    except Error as e:
        logging.error(f"Erreur lors de l'exécution de la requête: {e}")
        return f"Erreur lors de l'exécution de la requête: {e}", 500
    finally:
        connection.close()
    data = pd.DataFrame(results, columns=['region', 'coal_emissions_total', 'gas_emissions_total', 'oil_emissions_total', 'hydro_emissions_total', 'renewable_emissions_total', 'nuclear_emissions_total'])
    return render_template('regions_energy_usage.html', data=data.to_dict(orient='list'), energy_source=energy_source)



@app.route('/energy-source-proportions')
def energy_source_proportions():
    country_or_region = request.args.get('country')
    connection = create_connection()
    if connection is None:
        return "Erreur de connexion à la base de données", 500
    try:
        with connection.cursor() as cursor:
            if country_or_region:
                cursor.execute("""
                SELECT 
                    SUM(coal_emissions) AS total_coal,
                    SUM(gas_emissions) AS total_gas,
                    SUM(oil_emissions) AS total_oil,
                    SUM(hydro_emissions) AS total_hydro,
                    SUM(renewable_emissions) AS total_renewables,
                    SUM(nuclear_emissions) AS total_nuclear
                FROM (
                    SELECT * FROM country WHERE country = %s
                    UNION ALL
                    SELECT * FROM world WHERE region = %s
                ) AS combined;
                """, (country_or_region, country_or_region))
            else:
                cursor.execute("""
                SELECT 
                    SUM(coal_emissions) AS total_coal,
                    SUM(gas_emissions) AS total_gas,
                    SUM(oil_emissions) AS total_oil,
                    SUM(hydro_emissions) AS total_hydro,
                    SUM(renewable_emissions) AS total_renewables,
                    SUM(nuclear_emissions) AS total_nuclear
                FROM country;
                """)
            results = cursor.fetchone()

            cursor.execute("SELECT DISTINCT country FROM country;")
            countries = [row[0] for row in cursor.fetchall()]

            cursor.execute("SELECT DISTINCT region FROM world;")
            regions = [row[0] for row in cursor.fetchall()]
    except Error as e:
        logging.error(f"Erreur lors de l'exécution de la requête: {e}")
        return "Erreur lors de l'exécution de la requête", 500
    finally:
        connection.close()
    
    if not results or all(v is None for v in results):
        results = (0, 0, 0, 0, 0, 0)

    data = dict(zip(['total_coal', 'total_gas', 'total_oil', 'total_hydro', 'total_renewables', 'total_nuclear'], results))

    return render_template('energy_proportions.html', data=data, country=country_or_region, countries=countries, regions=regions)


if __name__ == '__main__':
    app.run(debug=True)
