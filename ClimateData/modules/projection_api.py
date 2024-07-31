from dotenv import load_dotenv
import geohelper as geo 
import os
import pandas as pd
import io

load_dotenv()
api_key = os.getenv("CLIMATE_API_KEY")

# Retrieve data from the Climate Data Service API
# https://beta.climatedataservice.com/v6/series/csv
# ?query=monthly%28maxtmp%2Cmax%29&
# from_date=2024-06-01T00%3A00%3A00.000Z&to_date=2050-01-01T00%3A00%3A00.000Z&latitude=6.1944&longitude=106.8229
def retrieveData(location, start_date, end_date):
    latlong = geo.get_lat_long(location)
    url = f'https://beta.climatedataservice.com/v6/series/csv?query=monthly%28maxtmp%2Cmax%29&from_date={start_date}T00%3A00%3A00.000Z&to_date={end_date}T00%3A00%3A00.000Z&latitude={latlong[0]}&longitude={latlong[1]}&apikey={api_key}'
    df = pd.read_csv(url, skiprows=12)
    return df
