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
def retrieveData(location, query_type, start_date, end_date):
    latlong = geo.get_lat_long(location)

    url_dictionary = {
    "num_days_above_100": f"?query=annually(exceed(maxtmp,365,37),mean)&from_date={start_date}T00%3A00%3A00.000Z&to_date={end_date}T00%3A00%3A00.000Z&latitude={latlong[0]}&longitude={latlong[1]}&apikey={api_key}",
    "num_days_above_90": f"?query=annually(exceed(maxtmp,365,32.2),mean)&from_date={start_date}T00%3A00%3A00.000Z&to_date={end_date}T00%3A00%3A00.000Z&latitude={latlong[0]}&longitude={latlong[1]}&apikey={api_key}",
    "num_days_above_80": f"?query=annually(exceed(maxtmp,365,26.7),mean)&from_date={start_date}T00%3A00%3A00.000Z&to_date={end_date}T00%3A00%3A00.000Z&latitude={latlong[0]}&longitude={latlong[1]}&apikey={api_key}",
    "tempmax": f"?query=monthly(maxtmp,max)&from_date={start_date}T00%3A00%3A00.000Z&to_date={end_date}T00%3A00%3A00.000Z&latitude={latlong[0]}&longitude={latlong[1]}&apikey={api_key}",
    "tempmin": f"?query=annually(mintmp,min)&from_date={start_date}T00%3A00%3A00.000Z&to_date={end_date}T00%3A00%3A00.000Z&latitude={latlong[0]}&longitude={latlong[1]}&apikey={api_key}",
    "precip": f"?query=annually(pr,sum)&from_date={start_date}T00%3A00%3A00.000Z&to_date={end_date}T00%3A00%3A00.000Z&latitude={latlong[0]}&longitude={latlong[1]}&apikey={api_key}",
    }
    url = f'https://beta.climatedataservice.com/v6/series/csv{url_dictionary[query_type]}'
    print(url)
    df = pd.read_csv(url, skiprows=12)
    return df

def retrieveDataByBoundingBox(from_latitude, to_latitude, from_longitude, to_longitude, query_type, start_date, end_date):
    url_dictionary = {
    "tempmax": f'https://beta.climatedataservice.com/v6/volume/json?query=annually(maxtmp,max)&from_date={start_date}T00:00:00.000Z&to_date={end_date}T00:00:00.000Z&from_latitude={from_latitude}&to_latitude={to_latitude}&from_longitude={from_longitude}&to_longitude={to_longitude}&apikey={api_key}'
    }
    url = f'https://beta.climatedataservice.com/v6/series/csv{url_dictionary[query_type]}'
    print(url)
    df = pd.read_csv(url, skiprows=12)
    return df