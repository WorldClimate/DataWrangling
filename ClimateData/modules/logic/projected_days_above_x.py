import pandas as pd
import projection_api as api

def calculate(location, query_type, year):
    raw_projection_df = api.retrieveData(location, query_type, f"{year}-08-01", "2050-06-01")

    # Process projected data
    raw_projection_df['datetime'] = pd.to_datetime(raw_projection_df['datetime'])
    raw_projection_df['year'] = raw_projection_df['datetime'].dt.year
    data_frame = raw_projection_df[['year','data']]

    # # Rename column to align with historical data
    data_frame.rename(columns={'data': query_type}, inplace=True)
    data_frame[query_type] = data_frame[query_type].round()

    return data_frame
