from dotenv import load_dotenv
import os
import pandas as pd
import io
import time
load_dotenv()
api_key = os.getenv("CLIMATE_API_KEY")

def retrieveDataByBoundingBox(from_latitude, to_latitude, from_longitude, to_longitude, query_type, start_date, end_date):
    url_dictionary = {
    "tempmax": f'?query=annually(flatten(flatten(maxtmp,1,mean),2,mean),mean)&from_date={start_date}T00:00:00.000Z&to_date={end_date}T00:00:00.000Z&from_latitude={from_latitude}&to_latitude={to_latitude}&from_longitude={from_longitude}&to_longitude={to_longitude}&apikey={api_key}'
    }
    url = f'https://beta.climatedataservice.com/v6/volume/csv{url_dictionary[query_type]}'
    print(url)
    df = pd.read_csv(url, skiprows=14)
    print(df.tail(10))

    return df