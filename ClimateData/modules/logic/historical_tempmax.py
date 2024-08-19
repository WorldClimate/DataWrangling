import pandas as pd

def calculate(data_frame, data_value, rolling_average):
    # Process historical data
    historical_df = data_frame[['datetime', data_value]]
    historical_df['datetime'] = pd.to_datetime(historical_df['datetime'])

    # Drop rows with missing data for the given data value
    historical_df.dropna(subset=[data_value], inplace=True)

    historical_df = historical_df.groupby([pd.Grouper(key='datetime', freq='1YE')], as_index=False).max()
    historical_df['datetime'] = pd.to_datetime(historical_df['datetime'])
    historical_df['year'] = historical_df['datetime'].dt.year

    # Drop rows with 2024 data
    historical_df = historical_df[historical_df['year'] < 2024]

    historical_df[data_value] = historical_df[data_value].map(lambda a: (a-32) * 5/9)

    return historical_df