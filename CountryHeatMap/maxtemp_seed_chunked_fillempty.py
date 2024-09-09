import json
import pandas as pd
from projection_api import retrieveDataByBoundingBox
import time
from ast import literal_eval
import json

countries = pd.read_csv('mean_maxtemp_countries.csv')
count=0
lowest=500
highest=-500
    
print(countries.head(10))
print('Starting to process countries')
for index, country in countries.iterrows():
    country_name = country['name']
    latlong = literal_eval(country['lat_long'])
    for total_year in range(2024, 2080):
            val = country[str(total_year)]
            if val > highest:
                highest = val
            if val < lowest:
                lowest = val
print(lowest)
print(highest)

