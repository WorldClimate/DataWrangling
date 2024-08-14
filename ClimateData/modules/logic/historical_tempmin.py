import pandas as pd

def calculate(data_frame, data_value, rolling_average):
    # Process historical data
    historical_df = data_frame[['datetime', data_value]]
    historical_df['datetime'] = pd.to_datetime(historical_df['datetime'])

    # Drop rows with missing data for the given data value
    historical_df.dropna(subset=[data_value], inplace=True)
    historical_df = historical_df.groupby([pd.Grouper(key='datetime', freq='1YE')], as_index=False).min()
    historical_df['datetime'] = pd.to_datetime(historical_df['datetime'])
    historical_df['year'] = historical_df['datetime'].dt.year
    historical_df[data_value] = historical_df[data_value].map(lambda a: (a-32) * 5/9)
    # Calculate Yearly Rolling Average
    historical_df[f'{rolling_average}_year_rolling_avg'] = historical_df[data_value].rolling(rolling_average).mean().round(2)

    # Drop first X rows that lack a rolling avg
    historical_df = historical_df.iloc[rolling_average:]
    return historical_df