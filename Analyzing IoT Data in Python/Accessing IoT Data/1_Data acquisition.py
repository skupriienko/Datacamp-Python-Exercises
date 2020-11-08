# Imports
import requests
import pandas as pd

# Download data from URL
res = requests.get(URL)

# Convert the result
data_temp = res.json()
print(data_temp)

# Convert json data to Dataframe
df_temp = pd.DataFrame(data_temp)

print(df_temp.head())