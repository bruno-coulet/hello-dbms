from flask import Flask, render_template
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

@app.route('/total-emissions')
def total_emissions():
    connection = create_connection()
    with connection.cursor() as cursor:
        cursor.execute("""
        SELECT country,
            (
                coal_emissions + gas_emissions + oil_emissions + hydro_emissions + renewable_emissions + nuclear_emissions
            ) AS total_emissions
        FROM country
        ORDER BY total_emissions DESC
        LIMIT 20;
        """)
        results = cursor.fetchall()
    connection.close()
    data = pd.DataFrame(results, columns=['country', 'total_emissions'])
    return render_template('total_emissions.html', data=data.to_dict(orient='list'))

@app.route('/coal-usage')
def coal_usage():
    connection = create_connection()
    with connection.cursor() as cursor:
        cursor.execute("""
        SELECT country, coal_emissions
        FROM country
        WHERE coal_emissions > 50
        ORDER BY coal_emissions DESC;
        """)
        results = cursor.fetchall()
    connection.close()
    data = pd.DataFrame(results, columns=['country', 'coal_emissions'])
    return render_template('coal_usage.html', data=data.to_dict(orient='list'))

@app.route('/energy-source-proportions')
def energy_source_proportions():
    connection = create_connection()
    with connection.cursor() as cursor:
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
    data = dict(zip(['total_coal', 'total_gas', 'total_oil', 'total_hydro', 'total_renewables', 'total_nuclear'], results))
    return render_template('energy_proportions.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
