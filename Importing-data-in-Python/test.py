import numpy as np
import pandas as pd


# Assign the filename: file
file = 'test.csv'

# Read the first 5 rows of the file into a DataFrame: data

data = pd.read_csv(file, header=0, sep=',', na_values='')
# Build a numpy array from the DataFrame: data_array
data_array = np.array(data)

# Print the datatype of data_array to the shell
print(type(data_array))


# Print the head of the DataFrame
print(data.head())
print(data_array)
