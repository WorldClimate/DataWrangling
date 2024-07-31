import projection_api as api
import pandas as pd

raw_projection_df = api.retrieveData("New York", "2024-01-01", "2025-01-01")

max_temp_df = raw_projection_df[['datetime','data']]

max_temp_df['datetime'] = pd.to_datetime(max_temp_df['datetime'])
max_temp_df = max_temp_df.groupby([pd.Grouper(key='datetime', freq='1M')]).max()
# print(df.tail(20))
print(max_temp_df.tail(20))