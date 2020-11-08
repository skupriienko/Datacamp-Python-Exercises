import pandas as pd

# Read file from json
df_env = pd.read_json("environmental.json")

# Print summary statistics
print(df_env.describe())