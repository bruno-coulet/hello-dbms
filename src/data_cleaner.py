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
