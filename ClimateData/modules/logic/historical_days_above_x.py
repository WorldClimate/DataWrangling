import pandas as pd

def calculate(data_frame, query_type, temperature):
    # Process historical data
    historical_df = data_frame[['datetime', 'tempmax']]
    historical_df['datetime'] = pd.to_datetime(historical_df['datetime'])

    historical_df = historical_df[historical_df['tempmax'] >= temperature]
    count_series = historical_df['tempmax'].groupby([historical_df['datetime'].dt.year]).count()
    final_df = count_series.to_frame().reset_index()
    final_df.columns = ['year', query_type]

    return final_df
