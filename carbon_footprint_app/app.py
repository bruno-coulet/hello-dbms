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
        ORDER BY total_emissions DESC;
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
    country = request.args.get('country')
    connection = create_connection()
    with connection.cursor(dictionary=True) as cursor:
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
        
        if not results or all(v is None for v in results):
            results = (0, 0, 0, 0, 0, 0)

        if country :
            cursor.execute('''SELECT
                            e.source AS "Source de production",
                            ROUND(c.percent_emission, 2) AS "pourcentage d’utilisation",
                            e.median_gco2_kwh AS "Médiane de gCO2/kWh",
                            ROUND((c.percent_emission / 100) * e.median_gco2_kwh, 2) AS "Contribution en émission gCO2/kWh"
                        FROM (
                            SELECT
                                'Charbon' AS source, coal_emissions AS percent_emission FROM country WHERE country = %s
                            UNION ALL
                            SELECT
                                'Gaz naturel', gas_emissions FROM country WHERE country = %s
                            UNION ALL
                            SELECT
                                'Pétrole', oil_emissions FROM country WHERE country = %s
                            UNION ALL
                            SELECT
                                'Hydro', hydro_emissions FROM country WHERE country = %s
                            UNION ALL
                            SELECT
                                'Renouvelable (Solaire)', renewable_emissions FROM country WHERE country = %s
                            UNION ALL
                            SELECT
                                'Nucléaire', nuclear_emissions FROM country WHERE country = %s
                        ) c
                        JOIN emissions e ON e.source = c.source;''',(country,) * 6)
        else:
            cursor.execute('''SELECT
                            e.source AS "Source de production",
                            ROUND(c.percent_emission, 2) AS "pourcentage d’utilisation",
                            e.median_gco2_kwh AS "Médiane de gCO2/kWh",
                            ROUND((c.percent_emission / 100) * e.median_gco2_kwh, 2) AS "Contribution en émission gCO2/kWh"
                        FROM (
                            SELECT
                                'Charbon' AS source, coal_emissions AS percent_emission FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Gaz naturel', gas_emissions FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Pétrole', oil_emissions FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Hydro', hydro_emissions FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Renouvelable (Solaire)', renewable_emissions FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Nucléaire', nuclear_emissions FROM country WHERE country = 'Albania'
                        ) c
                        JOIN emissions e ON e.source = c.source;''')  

        emission_contribution_data = cursor.fetchall()  

    
    connection.close()
    data = dict(zip(['total_coal', 'total_gas', 'total_oil', 'total_hydro', 'total_renewables', 'total_nuclear'], results))
    countries = get_countries()

    
    return render_template('energy_proportions.html', emission_contribution_data=emission_contribution_data , data=data, country=country, countries=countries)

@app.route('/emission-contribution')
def emission_contribution():
    country = request.args.get('country')
    connection = create_connection()
    with connection.cursor(dictionary=True) as cursor:
        if country :
            cursor.execute('''SELECT
                            e.source AS "Source de production",
                            ROUND(c.percent_emission, 2) AS "pourcentage d’utilisation",
                            e.median_gco2_kwh AS "Médiane de gCO2/kWh",
                            ROUND((c.percent_emission / 100) * e.median_gco2_kwh, 2) AS "Contribution en émission gCO2/kWh"
                        FROM (
                            SELECT
                                'Charbon' AS source, coal_emissions AS percent_emission FROM country WHERE country = %s
                            UNION ALL
                            SELECT
                                'Gaz naturel', gas_emissions FROM country WHERE country = %s
                            UNION ALL
                            SELECT
                                'Pétrole', oil_emissions FROM country WHERE country = %s
                            UNION ALL
                            SELECT
                                'Hydro', hydro_emissions FROM country WHERE country = %s
                            UNION ALL
                            SELECT
                                'Renouvelable (Solaire)', renewable_emissions FROM country WHERE country = %s
                            UNION ALL
                            SELECT
                                'Nucléaire', nuclear_emissions FROM country WHERE country = %s
                        ) c
                        JOIN emissions e ON e.source = c.source;''',(country,) * 6)
        else:
            cursor.execute('''SELECT
                            e.source AS "Source de production",
                            ROUND(c.percent_emission, 2) AS "pourcentage d’utilisation",
                            e.median_gco2_kwh AS "Médiane de gCO2/kWh",
                            ROUND((c.percent_emission / 100) * e.median_gco2_kwh, 2) AS "Contribution en émission gCO2/kWh"
                        FROM (
                            SELECT
                                'Charbon' AS source, coal_emissions AS percent_emission FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Gaz naturel', gas_emissions FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Pétrole', oil_emissions FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Hydro', hydro_emissions FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Renouvelable (Solaire)', renewable_emissions FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Nucléaire', nuclear_emissions FROM country WHERE country = 'Albania'
                        ) c
                        JOIN emissions e ON e.source = c.source;''')  

        emission_contribution_data = cursor.fetchall()  
    connection.close()  # Fermer la connexion à la base de données

    return render_template('emission-contribution.html', emission_contribution_data=emission_contribution_data , country=country)

if __name__ == '__main__':
    app.run(debug=True)
