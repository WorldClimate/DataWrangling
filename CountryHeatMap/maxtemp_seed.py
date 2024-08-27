import json
import pandas as pd
from projection_api import retrieveDataByBoundingBox
import time
from ast import literal_eval
import json

countries = pd.read_csv('maxtemp_countries.csv')
already_processed = json.load(open('already_processed.json'))
print(already_processed)
from_year = 2024
to_year = 2080
    
print(countries.head(10))
print('Starting to process countries')
for index, country in countries.iterrows():
    country_name = country['name']
    if country_name in already_processed:
        print('Skipping - ' + country_name)
        continue
    latlong = literal_eval(country['lat_long'])
    print(f'Processing - {country_name}')
    try:
        projection_df = retrieveDataByBoundingBox(latlong[1], latlong[3], latlong[0], latlong[2], 'tempmax', f'{from_year}-01-02', f'{to_year-1}-12-31')
    except:
        print(f'Error processing - {country_name}')
        continue
    for year in range(from_year, to_year):
        countries.loc[countries['name'] == country_name, str(year)] = projection_df.loc[pd.to_datetime(projection_df['datetime']).dt.year == year, 'data'].values[0]
    print(countries.head(10))
    
    countries.to_csv('maxtemp_countries.csv', index=False)
    already_processed.append(country_name)
    with open('maxtemp_already_processed.json', 'w') as file:
        json.dump(already_processed, file)
    time.sleep(10)
