# Import pandas
import pandas as pd

# Load URL to Dataframe
df_temp = pd.read_json(URL)

# Print first 5 rows
print(df_temp.head())

# Print datatypes
print(df_temp.dtypes)