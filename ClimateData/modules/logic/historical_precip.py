import pandas as pd

def calculate(data_frame, rolling_average):
    # Process historical data
    historical_df = data_frame[['datetime', 'precip']]
    historical_df['datetime'] = pd.to_datetime(historical_df['datetime'])
    # Extract year from datetime column
    historical_df['year'] = historical_df['datetime'].dt.year

    # convert inches to mm
    historical_df['precip'] = historical_df['precip'] * 25.4

    # Count the number of days above the temperature threshold, fill in empty years with 0
    # aggregated_df = historical_df.groupby([historical_df['datetime'].dt.year]).sum().reset_index()
    aggregated_df = historical_df.groupby('year')['precip'].sum().reset_index()

    aggregated_df[f'{rolling_average}_year_rolling_avg'] = aggregated_df['precip'].rolling(rolling_average).mean().round(4)

    # Drop first X rows that lack a rolling avg
    aggregated_df = aggregated_df.iloc[rolling_average:]

    return aggregated_df
