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


@app.route('/countries')
def get_countries():
    connection = create_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT country FROM country;")
        countries = [row[0] for row in cursor.fetchall()]
    connection.close()
    return countries

@app.route('/energy-usage')
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
    return render_template('energy_usage.html', data=data.to_dict(orient='list'), energy_source=energy_source)

@app.route('/energy-source-proportions')
def energy_source_proportions():
    country = request.args.get('country')
    connection = create_connection()
    with connection.cursor() as cursor:
        if country:
            cursor.execute("""
            SELECT 
                SUM(coal_emissions) AS total_coal,
                SUM(gas_emissions) AS total_gas,
                SUM(oil_emissions) AS total_oil,
                SUM(hydro_emissions) AS total_hydro,
                SUM(renewable_emissions) AS total_renewables,
                SUM(nuclear_emissions) AS total_nuclear
            FROM country
            WHERE country = %s;
            """, (country,))
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
    connection.close()
    
    if not results or all(v is None for v in results):
        results = (0, 0, 0, 0, 0, 0)

    data = dict(zip(['total_coal', 'total_gas', 'total_oil', 'total_hydro', 'total_renewables', 'total_nuclear'], results))
    countries = get_countries()

    return render_template('energy_proportions.html', data=data, country=country, countries=countries)

if __name__ == '__main__':
    app.run(debug=True)
