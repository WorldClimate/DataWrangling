import pandas as pd

input_file = '../Oxford/Raw/historical_daily_raw.csv'
temperature = 90
query_type = 'num_days_above_90'

#Import raw file
data_frame = pd.read_csv(input_file)

historical_df = data_frame[['datetime', 'tempmax']]
historical_df['datetime'] = pd.to_datetime(historical_df['datetime'])

historical_df = historical_df[historical_df['tempmax'] >= temperature]
count_series = historical_df['tempmax'].groupby([historical_df['datetime'].dt.year]).count().reindex(range(1980, 2025), fill_value=0)

final_df = count_series.to_frame().reset_index()
final_df.columns = ['year', query_type]

print(final_df)