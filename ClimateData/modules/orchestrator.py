import projection_api as api
import pandas as pd

# Get Input from User
city_name = input("What is the City?")
data_value = 'tempmax'

# Retrieve the projected data
raw_projection_df = api.retrieveData(city_name, "2024-08-01", "2050-06-01")
# Process projected data
projected_max_temp_df = raw_projection_df[['datetime','data']]
projected_max_temp_df['datetime'] = pd.to_datetime(projected_max_temp_df['datetime'])
projected_max_temp_df = projected_max_temp_df.groupby([pd.Grouper(key='datetime', freq='1M')]).max()

# Rename column to align with historical data
projected_max_temp_df.rename(columns={'data': data_value}, inplace=True)

# Save the processed data
projected_max_temp_df.to_csv('../'+city_name+'/Processed/projected_'+data_value+'_monthly.csv')
projected_max_temp_df.to_json('../'+city_name+'/Processed/projected_'+data_value+'_monthly.json', orient='table')

# Retrieve the historical data
input_file = '../'+city_name+'/Raw/historical_daily_raw.csv'
raw_historical_df = pd.read_csv(input_file)

# Process historical data
historical_max_temp_df = raw_historical_df[['datetime',data_value]]
historical_max_temp_df['datetime'] = pd.to_datetime(historical_max_temp_df['datetime'])
historical_max_temp_df = historical_max_temp_df.groupby([pd.Grouper(key='datetime', freq='1M')]).max()
historical_max_temp_df[data_value] = historical_max_temp_df[data_value].map(lambda a: (a-32) * 5/9)

# Save the processed data
output_location = '../'+city_name+'/Processed/historical_'+data_value+'_monthly'
historical_max_temp_df.to_csv(output_location+'.csv')
historical_max_temp_df.to_json(output_location+'.json', orient='table')

# Combine the historical & projected data
combined_df = pd.concat([historical_max_temp_df, projected_max_temp_df])

# calculate historical average over last two years
output_location = '../'+city_name+'/Processed/combined_'+data_value
combined_df.to_csv(output_location+'.csv')
combined_df.to_json(output_location+'.json', orient='table')
# determine if projected temp needs offset

# apply offset to projected data

# Combine the historical & projected data