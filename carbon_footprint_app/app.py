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
    return render_template('index.html')

@app.context_processor
def inject_countries():
    def get_countries():
        connection = create_connection()
        if connection is None:
            return []
        with connection.cursor() as cursor:
            cursor.execute("SELECT DISTINCT country FROM country;")
            countries = [row[0] for row in cursor.fetchall()]
            cursor.execute("SELECT DISTINCT region FROM world;")
            regions = [row[0] for row in cursor.fetchall()]
        connection.close()
        return countries
    return dict(get_countries=get_countries)

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

    return render_template(
        'energy_proportions.html',
        data=data,
        country=country_or_region,
        countries=countries,
        regions=regions
        )

@app.route('/selected_country_total_emissions')
def selected_country_total_emissions():
    country = request.args.get('country')  # Récupération du pays sélectionné
    connection = create_connection()
    
    with connection.cursor() as cursor:
        if country:
            cursor.execute("""
                SELECT 
                    SUM(coal_percentage) AS total_coal,
                    SUM(gas_percentage) AS total_gas,
                    SUM(oil_percentage) AS total_oil,
                    SUM(hydro_percentage) AS total_hydro,
                    SUM(renewable_percentage) AS total_renewables,
                    SUM(nuclear_percentage) AS total_nuclear
                FROM percentage
                WHERE country = %s;
            """, (country,))
        else:
            cursor.execute("""
                SELECT 
                    SUM(coal_percentage) AS total_coal,
                    SUM(gas_percentage) AS total_gas,
                    SUM(oil_percentage) AS total_oil,
                    SUM(hydro_percentage) AS total_hydro,
                    SUM(renewable_percentage) AS total_renewables,
                    SUM(nuclear_percentage) AS total_nuclear
                FROM percentage;
            """)
        results = cursor.fetchone()
        # Récupération des listes de pays
        cursor.execute("SELECT DISTINCT country FROM percentage;")
        countries = [row[0] for row in cursor.fetchall()]
        # Récupération des régions
        cursor.execute("SELECT DISTINCT region FROM world;")
        regions = [row[0] for row in cursor.fetchall()]
    connection.close()

    # Si aucun résultat trouvé ou données vides
    if not results or all(v is None for v in results):
        results = (0, 0, 0, 0, 0, 0)
    # Transformation des résultats en dictionnaire
    data = dict(zip(['total_coal', 'total_gas', 'total_oil', 'total_hydro', 'total_renewables', 'total_nuclear'], results))
    # La fonction get_countries est maintenant disponible dans le template
    return render_template(
        'selected_country_total_emissions.html',
        data=data,
        selected_country=country,
        countries=countries,
        regions=regions
    )

if __name__ == '__main__':
    app.run(debug=True)
