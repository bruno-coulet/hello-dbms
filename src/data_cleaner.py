# data_cleaner.py

class DataCleaner:
    @staticmethod
    def clean_value(val):
        if isinstance(val, str):
            val = val.strip().replace(',', '.')
        try:
            return float(val) if val not in ["", "N/A", "NaN"] else None
        except ValueError:
            return None

    @staticmethod
    def clean_data(df):
        df['Country'] = df['Country'].str.strip().apply(lambda x: x.replace("'", "''"))
        df['Region'] = df['Region'].str.strip().apply(lambda x: x.replace("'", "''"))
        columns_to_clean = [col for col in df.columns if col not in ['Country', 'Region']]
        df[columns_to_clean] = df[columns_to_clean].map(DataCleaner.clean_value)
        return df

    @staticmethod
    def clean_table_columns(cursor, table_name, logger=None):
        # Requête SQL pour modifier les colonnes de la table
        alter_query = f"""
        ALTER TABLE {table_name}
            MODIFY COLUMN `Population` INT,
            MODIFY COLUMN `Area (sq. mi.)` FLOAT,
            MODIFY COLUMN `Pop. Density (per sq. mi.)` FLOAT,
            MODIFY COLUMN `Coastline (coast/area ratio)` FLOAT,
            MODIFY COLUMN `Net migration` FLOAT,
            MODIFY COLUMN `Infant mortality (per 1000 births)` FLOAT,
            MODIFY COLUMN `GDP ($ per capita)` FLOAT,
            MODIFY COLUMN `Literacy (%)` FLOAT,
            MODIFY COLUMN `Phones (per 1000)` FLOAT,
            MODIFY COLUMN `Arable (%)` FLOAT,
            MODIFY COLUMN `Crops (%)` FLOAT,
            MODIFY COLUMN `Other (%)` FLOAT,
            MODIFY COLUMN `Birthrate` FLOAT,
            MODIFY COLUMN `Deathrate` FLOAT,
            MODIFY COLUMN `Agriculture` FLOAT,
            MODIFY COLUMN `Industry` FLOAT,
            MODIFY COLUMN `Service` FLOAT;
        """

        try:
            cursor.execute(alter_query)
            if logger:
                logger.log_step("Table Alteration", f"Columns in table '{table_name}' modified successfully.", success=True)
        except Exception as e:
            if logger:
                logger.log_step("Table Alteration", f"Error altering columns in table '{table_name}': {str(e)}", success=False)
            raise Exception(f"Error during ALTER TABLE: {str(e)}")
