# Import pandas
import pandas as pd

# Load URL to Dataframe
df_temp = pd.read_json(URL)

# Save dataframe as json
df_temp.to_json("temperature.json", orient='records')

# Save dataframe as csv
df_temp.to_csv("temperature.csv", index=False)