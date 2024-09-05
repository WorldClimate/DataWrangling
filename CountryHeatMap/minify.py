import pandas as pd
import numpy as np
import json
# Divide all entries by 100 to fit map gradient
countries = pd.read_csv('maxtemp_countries_v2.csv')
columns_to_divide = countries.columns[3:]  # Assuming the columns '2024' to '2080' are in positions 2 to end
countries[columns_to_divide] = countries[columns_to_divide] / 100
print(countries.head(10))
countries.to_csv('maxtemp_countries_minified_v2.csv', index=False)
