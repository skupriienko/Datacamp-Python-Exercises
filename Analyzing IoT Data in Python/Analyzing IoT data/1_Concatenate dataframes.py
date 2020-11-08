# Rename the columns
temperature.columns = ["temperature"]
humidity.columns = ["humidity"]
windspeed.columns = ["windspeed"]

# Create list of dataframes
df_list = [temperature, humidity, windspeed]

# Concatenate files
environment = pd.concat(df_list, axis=1)

# Print dataframe
print(environment.head())