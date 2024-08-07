import projection_api as api
import pandas as pd
import shutil
import sys
import logic.historical_tempmax as hist_tempmax
import logic.historical_tempmin as hist_tempmin

def orchestrate(location, query_type, rolling_average):

    # Get Input from Command Line
    # city_name = sys.argv[1]
    # data_value = sys.argv[2]
    # rolling_average = int(sys.argv[3])

    # Get Input from User
    # city_name = input("What is the City?")
    # data_value = input("What is the Data value you would like? (tempmax, tempmin, precip)")
    # rolling_average = int(input("What is the rolling average you would like?"))
    # data_value = 'tempmax'
    year = 2024

    # Retrieve the projected data
    raw_projection_df = api.retrieveData(location, query_type, f"{year}-08-01", "2050-06-01")

    # Process projected data
    projected_df = raw_projection_df[['datetime','data']]
    projected_df['datetime'] = pd.to_datetime(projected_df['datetime'])
    projected_df = projected_df.groupby([pd.Grouper(key='datetime', freq='1YE')],as_index=False).max()
    projected_df['datetime'] = pd.to_datetime(projected_df['datetime'])
    projected_df['year'] = projected_df['datetime'].dt.year

    # Rename column to align with historical data
    projected_df.rename(columns={'data': query_type}, inplace=True)

    # Calculate Yearly Rolling Average
    projected_df['yearly_rolling_avg'] = projected_df[query_type].rolling(rolling_average).mean().round(2)

    # Drop first X rows that lack a rolling avg
    projected_df = projected_df.iloc[rolling_average:]

    # Save the processed data
    projected_df.to_csv('../'+location['city_name']+'/Processed/projected_'+query_type+'_monthly.csv')
    projected_df.to_json('../'+location['city_name']+'/Processed/projected_'+query_type+'_monthly.json', orient='table')

    # Retrieve the historical data
    input_file = '../'+location['city_name']+'/Raw/historical_daily_raw.csv'
    raw_historical_df = pd.read_csv(input_file)

    # Call Historical data API
    if(query_type == 'tempmax'):
        historical_df = hist_tempmax.calculate(raw_historical_df, query_type, rolling_average)

    elif(query_type == 'tempmin'):
        historical_df = hist_tempmin.calculate(raw_historical_df, query_type, rolling_average)

    # Save the processed data
    output_location = '../'+location['city_name']+'/Processed/historical_'+query_type+'_monthly'
    historical_df.to_csv(output_location+'.csv')
    historical_df.to_json(output_location+'.json', orient='table')

    # Combine the historical & projected data
    combined_df = pd.concat([historical_df, projected_df])
    output_location = '../'+location['city_name']+'/Processed/combined_'+query_type
    combined_df.to_csv(output_location+'.csv')
    combined_df.to_json(output_location+'.json', orient='table')

    # Copy the processed data to the web app
    hyphenated_city = location['city_name'].replace(' ', '-')
    source_file = open(output_location+'.json', 'rb')
    destination_file = open('../../../Climate Platform/React/ClimatePlatform/data/'+hyphenated_city+'/combined_'+query_type+'.json', 'wb')
    shutil.copyfileobj(source_file, destination_file)
    print('Data copied to web app')
    return True