import pandas as pd

def calculate(data_frame, year):
    dew_df = data_frame[['datetime','dew']]
    dew_df['datetime'] = pd.to_datetime(dew_df['datetime'])
    dew_df['year'] = pd.to_datetime(dew_df['datetime']).dt.year

    # Drop rows with 2024 data
    dew_df = dew_df[dew_df['year'] < year]

    dew_df['dew'] = dew_df['dew'].map(lambda a: (a-32) * 5/9)

    aggregated_df = dew_df.groupby('year')['dew'].mean().reset_index()
    return aggregated_df