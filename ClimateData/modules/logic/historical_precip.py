import pandas as pd

def calculate(data_frame, rolling_average):
    # Process historical data
    historical_df = data_frame[['datetime', 'precip']]
    historical_df['datetime'] = pd.to_datetime(historical_df['datetime'])

    # Extract year from datetime column
    historical_df['year'] = historical_df['datetime'].dt.year

    # Drop rows with 2024 data
    historical_df = historical_df[historical_df['year'] < 2024]

    # convert inches to mm
    historical_df['precip'] = historical_df['precip'] * 25.4

    aggregated_df = historical_df.groupby('year')['precip'].sum().reset_index()

    return aggregated_df
