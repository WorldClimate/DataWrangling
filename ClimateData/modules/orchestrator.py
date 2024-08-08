import pandas as pd
import shutil
import sys
import logic.historical_tempmax as hist_tempmax
import logic.historical_tempmin as hist_tempmin
import logic.historical_days_above_x as hist_days_above_x
import logic.projected_tempmax as projected_tempmax
import logic.projected_tempmin as projected_tempmin
import logic.projected_days_above_x as projected_days_above_x

def orchestrate(location, query_type, rolling_average):

    year = 2024
    # Retrieve the historical data
    input_file = '../'+location['city_name']+'/Raw/historical_daily_raw.csv'
    raw_historical_df = pd.read_csv(input_file)

    # Call methodologies
    if(query_type == 'tempmax'):
        historical_df = hist_tempmax.calculate(raw_historical_df, query_type, rolling_average)
        projected_df = projected_tempmax.calculate(location, query_type, year, rolling_average)
    elif(query_type == 'tempmin'):
        historical_df = hist_tempmin.calculate(raw_historical_df, query_type, rolling_average)
        projected_df = projected_tempmin.calculate(location, query_type, year, rolling_average)
    elif(query_type == 'num_days_above_80'):
        historical_df = hist_days_above_x.calculate(raw_historical_df, query_type, 80)
        projected_df = projected_days_above_x.calculate(location, query_type, year)
    elif(query_type == 'num_days_above_90'):
        historical_df = hist_days_above_x.calculate(raw_historical_df, query_type, 90)
        projected_df = projected_days_above_x.calculate(location, query_type, year)
    elif(query_type == 'num_days_above_100'):
        historical_df = hist_days_above_x.calculate(raw_historical_df, query_type, 100)
        projected_df = projected_days_above_x.calculate(location, query_type, year)

    # Save the processed data
    projected_output_location = '../'+location['city_name']+'/Processed/projected_'+query_type
    historical_output_location = '../'+location['city_name']+'/Processed/historical_'+query_type

    projected_df.to_csv(projected_output_location+'.csv')
    projected_df.to_json(projected_output_location+'.json', orient='table')

    historical_df.to_csv(historical_output_location+'.csv')
    historical_df.to_json(historical_output_location+'.json', orient='table')

    # Combine the historical & projected data
    combined_df = pd.concat([historical_df, projected_df])
    combined_output_location = '../'+location['city_name']+'/Processed/combined_'+query_type
    combined_df.to_csv(combined_output_location+'.csv')
    combined_df.to_json(combined_output_location+'.json', orient='table')

    # Copy the processed data to the web app
    hyphenated_city = location['city_name'].replace(' ', '-')
    source_file = open(combined_output_location+'.json', 'rb')
    destination_file = open('../../../Climate Platform/React/ClimatePlatform/data/'+hyphenated_city+'/combined_'+query_type+'.json', 'wb')
    shutil.copyfileobj(source_file, destination_file)
    print('Data copied to web app')
    return True