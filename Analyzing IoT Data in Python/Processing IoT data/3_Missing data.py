# Print head of the DataFrame
print(data.head())

# Drop missing rows
data_clean = data.dropna()
print(data_clean.head())


# Print head of the DataFrame
print(data.head())

# Forward-fill missing values
data_clean = data.fillna(method='ffill')
print(data_clean.head())