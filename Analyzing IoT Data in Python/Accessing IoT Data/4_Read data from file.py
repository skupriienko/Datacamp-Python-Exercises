import pandas as pd

# Read file
df_env = pd.read_csv("environmental.csv", parse_dates=['timestamp'])

# Print head
print(df_env.head())

# Print dataframe info
print(df_env.info())


import pandas as pd

# Read file
df_env = pd.read_json("environmental.json")

# Print head
print(df_env.head())

# Print dataframe info
print(df_env.info())