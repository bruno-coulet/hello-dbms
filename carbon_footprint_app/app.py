
from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error
import plotly.express as px
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


@app.route('/world-map')
def world_map():
    # Récupérer la source d'énergie depuis les paramètres de la requête
    energy_source = request.args.get('source', 'coal_emissions')  # Par défaut, charbon

    # Dictionnaire pour les noms en français des sources d'énergie
    energy_source_translation = {
        'coal_emissions': 'du charbon',
        'gas_emissions': 'du gaz',
        'oil_emissions': 'du pétrole',
        'hydro_emissions': 'de l\'hydroélectrique',
        'renewable_emissions': 'des énergies renouvelables',
        'nuclear_emissions': 'du nucléaire'
    }

    # Connexion à la base de données
    connection = create_connection()
    if connection is None:
        return "Erreur de connexion à la base de données", 500
    
    try:
        with connection.cursor() as cursor:
            # Exécuter la requête pour récupérer les pourcentages d'utilisation de la source d'énergie par pays
            cursor.execute(f"SELECT country, {energy_source} FROM country")
            results = cursor.fetchall()
    except Error as e:
        logging.error(f"Erreur lors de l'exécution de la requête: {e}")
        return f"Erreur lors de l'exécution de la requête: {e}", 500
    finally:
        connection.close()

    # Convertir les résultats en DataFrame pandas
    df = pd.DataFrame(results, columns=['country', 'energy_usage_percentage'])
    
    # Formater le pourcentage en ajoutant '%' à la valeur
    df['energy_usage_percentage'] = df['energy_usage_percentage'].apply(lambda x: f"{x:.2f}%")
    
    # Ajuster les valeurs à un format numérique pour l'échelle de couleurs
    df['energy_usage_percentage_numeric'] = df['energy_usage_percentage'].apply(lambda x: float(x.strip('%')) if isinstance(x, str) else x)

    # Définir les dégradés de couleurs en fonction de la source d'énergie
    color_scales = {
        'coal_emissions': ["#ffffff", "#000000"],  # Dégradé pour charbon (de blanc à noir)
        'gas_emissions': ["#ffffff", "#ff4f00"],   # Dégradé pour gaz (orange)
        'oil_emissions': ["#ffffff", "#b4533f"],   # Dégradé pour pétrole (marron)
        'hydro_emissions': ["#ffffff", "#00bfff"],  # Dégradé pour hydroélectrique (bleu)
        'renewable_emissions': ["#ffffff", "#006400"],  # Dégradé pour renouvelables (vert)
        'nuclear_emissions': ["#ffffff", "#4b0082"]  # Dégradé pour nucléaire (violet)
    }

    # Sélectionner le dégradé de couleur approprié en fonction de la source d'énergie
    color_scale = color_scales.get(energy_source, ["white", "black"])

    # Utilisation de Plotly Express pour créer la carte choroplèthe
    fig = px.choropleth(df, 
                        locations="country", 
                        locationmode="country names", 
                        color="energy_usage_percentage_numeric", 
                        hover_name="country",  # Garde le nom du pays pour la carte
                        hover_data={"energy_usage_percentage": True, "country": False, "energy_usage_percentage_numeric": False},  # Supprime 'energy_usage_percentage_numeric' du hover
                        color_continuous_scale=color_scale,  # Applique le dégradé de couleur approprié
                        range_color=[0, 100],  # Spécifie que l'échelle de couleurs va de 0 à 100
                        labels={'energy_usage_percentage': 'Pourcentage d utilisation de la source d énergie'}, 
                        title=f"Utilisation {energy_source_translation.get(energy_source, 'Source d énergie inconnue')}")
    
    # Modifier le titre de la légende
    fig.update_layout(coloraxis_colorbar_title="Pourcentage d'utilisation de la source d'énergie")

    # Centrer le titre du graphique
    fig.update_layout(title_x=0.5)  # Centrer le titre horizontalement
    
    # Générer le code HTML du graphique
    graph_html = fig.to_html(full_html=False)

    # Rendre la page avec le graphique
    return render_template('world_map.html', graph_html=graph_html, energy_source=energy_source)


@app.route('/emission_contribution')
def emission_contribution():
    country_or_region = request.args.get('country')
    connection = create_connection()
    with connection.cursor(dictionary=True) as cursor:
        if country_or_region :
            cursor.execute('''SELECT
                            e.source AS "Source de production",
                            ROUND(c.percent_emission, 2) AS "pourcentage d’utilisation",
                            e.median_gco2_kwh AS "Médiane de gCO2/kWh",
                            ROUND((c.percent_emission / 100) * e.median_gco2_kwh, 2) AS "Contribution en émission gCO2/kWh"
                        FROM (
                            SELECT
                                'Coal' AS source, coal_emissions AS percent_emission FROM (
                                        SELECT * FROM country WHERE country = %s
                                        UNION 
                                        SELECT * FROM world WHERE region = %s
                                    ) AS combined
                            UNION 
                            SELECT
                                'Natural gas', gas_emissions FROM  (
                                        SELECT * FROM country WHERE country = %s
                                        UNION 
                                        SELECT * FROM world WHERE region = %s
                                    ) AS combined
                            UNION 
                            SELECT
                                'Oil', oil_emissions FROM (
                                        SELECT * FROM country WHERE country = %s
                                        UNION 
                                        SELECT * FROM world WHERE region = %s
                                    ) AS combined
                            UNION 
                            SELECT
                                'Hydro', hydro_emissions FROM (
                                        SELECT * FROM country WHERE country = %s
                                        UNION 
                                        SELECT * FROM world WHERE region = %s
                                    ) AS combined
                            UNION 
                            SELECT
                                'Renewable Solar', renewable_emissions FROM  (
                                        SELECT * FROM country WHERE country = %s
                                        UNION 
                                        SELECT * FROM world WHERE region = %s
                                    ) AS combined
                            UNION 
                            SELECT
                                'Nuclear', nuclear_emissions FROM (
                                        SELECT * FROM country WHERE country = %s
                                        UNION 
                                        SELECT * FROM world WHERE region = %s
                                    ) AS combined
                        ) c
                        JOIN emissions e ON e.source = c.source;''',(country_or_region,) * 12  )
        else:
            cursor.execute('''SELECT
                            e.source AS "Source de production",
                            ROUND(c.percent_emission, 2) AS "pourcentage d’utilisation",
                            e.median_gco2_kwh AS "Médiane de gCO2/kWh",
                            ROUND((c.percent_emission / 100) * e.median_gco2_kwh, 2) AS "Contribution en émission gCO2/kWh"
                        FROM (
                            SELECT
                                'Coal' AS source, coal_emissions AS percent_emission FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Natural gas', gas_emissions FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Oil', oil_emissions FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Hydro', hydro_emissions FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Renewable Solar', renewable_emissions FROM country WHERE country = 'Albania'
                            UNION ALL
                            SELECT
                                'Nuclear', nuclear_emissions FROM country WHERE country = 'Albania'
                        ) c
                        JOIN emissions e ON e.source = c.source;''')  

        emission_contribution_data = cursor.fetchall()  
        
        cursor.execute("SELECT DISTINCT country FROM country;")
        countries = [row['country'] for row in cursor.fetchall()]
        cursor.execute("SELECT DISTINCT region FROM world;")
        regions = [row['region'] for row in cursor.fetchall()]

    connection.close() 

    return render_template('emission_contribution.html', country=country_or_region , emission_contribution_data=emission_contribution_data , countries=countries, regions=regions)



@app.route('/total_emission')
def total_emission():
    annual_total_emission = None
    country = request.args.get('country')
    connection = create_connection()
    with connection.cursor(dictionary=True) as cursor:
        if country :
            cursor.execute('''SELECT
         c.country,
         (
             (c.coal_emissions / 100) * e1.median_gCO2_kWh +
             (c.gas_emissions / 100) * e2.median_gCO2_kWh +
             (c.oil_emissions / 100) * e3.median_gCO2_kWh +
             (c.hydro_emissions / 100) * e4.median_gCO2_kWh +
             (c.renewable_emissions / 100) * e5.median_gCO2_kWh +
             (c.nuclear_emissions / 100) * e6.median_gCO2_kWh
         ) AS total_contribution_gCO2_kWh
     FROM
         country c
     JOIN
         emissions e1 ON e1.source = 'Coal'
     JOIN
         emissions e2 ON e2.source = 'Natural gas'
     JOIN
         emissions e3 ON e3.source = 'Oil'
     JOIN
         emissions e4 ON e4.source = 'Hydro'
     JOIN
         emissions e5 ON e5.source = 'Renewable Solar'
     JOIN
         emissions e6 ON e6.source = 'Nuclear'
     WHERE c.country = %s;''',(country,))
        else:
            cursor.execute('''SELECT
         c.country,
         (
             (c.coal_emissions / 100) * e1.median_gCO2_kWh +
             (c.gas_emissions / 100) * e2.median_gCO2_kWh +
             (c.oil_emissions / 100) * e3.median_gCO2_kWh +
             (c.hydro_emissions / 100) * e4.median_gCO2_kWh +
             (c.renewable_emissions / 100) * e5.median_gCO2_kWh +
             (c.nuclear_emissions / 100) * e6.median_gCO2_kWh
         ) AS total_contribution_gCO2_kWh
     FROM
         country c
     JOIN
         emissions e1 ON e1.source = 'Coal'
     JOIN
         emissions e2 ON e2.source = 'Natural gas'
     JOIN
         emissions e3 ON e3.source = 'Oil'
     JOIN
         emissions e4 ON e4.source = 'Hydro'
     JOIN
         emissions e5 ON e5.source = 'Renewable Solar'
     JOIN
         emissions e6 ON e6.source = 'Nuclear'
     WHERE c.country = 'Albania';''')  

        result_total_emission = cursor.fetchone() 

        if result_total_emission :
            total_emission = result_total_emission['total_contribution_gCO2_kWh'] 
            total_emission = round(total_emission, 2)
            annual_total_emission = total_emission * 24 *365 
        else :
            total_emission = None
        
        cursor.execute("SELECT DISTINCT country FROM country;")
        countries = [row['country'] for row in cursor.fetchall()]

    connection.close() 

    return render_template('total_emission.html', country=country ,annual_total_emission=annual_total_emission , total_emission=total_emission , countries=countries)



if __name__ == '__main__':
    app.run(debug=True)