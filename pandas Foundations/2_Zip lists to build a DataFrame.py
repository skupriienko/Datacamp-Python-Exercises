#  In this exercise, you're going to make a pandas DataFrame 
# of the top three countries to win gold medals since 1896 
# by first building a dictionary. list_keys contains the column 
# names 'Country' and 'Total'. list_values contains the full names 
# of each country and the number of gold medals awarded. 
# The values have been taken from Wikipedia (https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table).

# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = list(zip(list_keys, list_values))

# Inspect the list using print()
print(zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)