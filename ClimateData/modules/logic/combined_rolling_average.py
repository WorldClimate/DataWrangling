import pandas as pd

def calculate(data_frame, rolling_average, field):
    data_frame[f'{rolling_average}_year_rolling_avg'] = data_frame[field].rolling(rolling_average).mean().round(4)
    return data_frame