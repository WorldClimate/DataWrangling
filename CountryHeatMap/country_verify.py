import json
import pandas as pd
from projection_api import retrieveDataByBoundingBox
import time
from ast import literal_eval
import json

# countries = pd.read_csv('maxtemp_test.csv')
from_year = 2050
to_year = 2055
    
# print(countries.head(10))
print('Starting to process countries')
latlong = literal_eval("[-12.17, 10.1, 4.27, 24.97]")
projection_df = retrieveDataByBoundingBox(latlong[1], latlong[3], latlong[0], latlong[2], 'tempmax', f'{from_year}-01-02', f'{to_year-1}-12-31')
projection_df.to_csv('maxtemp_mali_test.csv', index=False)
