import pandas as pd

def calculate(data_frame, query_type, temperature):
    # Process historical data
    historical_df = data_frame[['datetime', 'tempmax']]
    historical_df['datetime'] = pd.to_datetime(historical_df['datetime'])

    historical_df = historical_df[historical_df['tempmax'] >= temperature]
    # Count the number of days above the temperature threshold, fill in empty years with 0
    count_series = historical_df['tempmax'].groupby([historical_df['datetime'].dt.year]).count().reindex(range(1980, 2025), fill_value=0)
    final_df = count_series.to_frame().reset_index()
    final_df.columns = ['year', query_type]
    
    # Drop rows with 2024 data
    final_df = final_df[final_df['year'] < 2024]

    return final_df
