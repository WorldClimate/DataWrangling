import json
import pandas as pd
from projection_api import retrieveDataByBoundingBox
import time
from ast import literal_eval
import json

countries = pd.read_csv('maxtemp_countries_v2.csv')
already_processed = json.load(open('maxtemp_already_processed.json'))
print(already_processed)
window = 1
from_year = 2024
to_year = 2080
total_years = to_year - from_year
modified_from = from_year
modified_to = from_year + window
print(f'Mod from - {modified_from}, Mod To - {modified_to}')
    
print(countries.head(10))
print('Starting to process countries')
for index, country in countries.iterrows():
    country_name = country['name']
    # if country_name in already_processed:
    #     print('Skipping - ' + country_name)
    #     continue
    print(f'Processing - {country_name}')
    latlong = literal_eval(country['lat_long'])
    for total_year in range(from_year, to_year, window):
        if pd.isnull(country[str(total_year)]) | pd.isnull(country[str(total_year + window - 1)]):
            modified_from = total_year
            modified_to = total_year + window
            print(f'Found an empty cell at {total_year}')
            print(f'Processing - {country_name} - {modified_from} TO {modified_to}')
            try:
                projection_df = retrieveDataByBoundingBox(latlong[1], latlong[3], latlong[0], latlong[2], 'tempmax', f'{modified_from}-01-02', f'{modified_to-1}-12-31')
            except:
                print(f'Error processing - {country_name}')
                time.sleep(10)
                continue
            for year in range(modified_from, modified_to):
                countries.loc[countries['name'] == country_name, str(year)] = projection_df.loc[pd.to_datetime(projection_df['datetime']).dt.year == year, 'data'].values[0]
            print(countries.head(10))
            print('Saving progress')
            countries.to_csv('maxtemp_countries_v2.csv', index=False)
            time.sleep(8)
        # Make sure we don't go over the limit
        if modified_to > to_year:
            modified_to = to_year
        if modified_from > to_year:
            modified_from = to_year
    modified_from = from_year
    modified_to = from_year + window
    

