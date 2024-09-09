import pandas as pd
import numpy as np
import json

# Divide all entries by 100 to fit map gradient
countries = pd.read_csv('mean_maxtemp_countries.csv')
columns_to_divide = countries.columns[3:]  # Assuming the columns '2024' to '2080' are in positions 2 to end
countries[columns_to_divide] = round(countries[columns_to_divide] / 100, 4)
print(countries.head(10))
countries.to_csv('mean_maxtemp_countries_minified.csv', index=False)
