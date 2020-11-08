# Import the python CSV module
import csv
import pandas as pd

# Create a python file object in read mode for the `baby_names.csv` file: csvfile
csvfile = open('contacts1.csv', 'r')


# Loop over a DictReader on the file
for row in pd.csv_reader(csvfile):
    # Print each row
    print(row)
    # Add the rank and name to the dictionary: baby_names
    baby_names[row['RANK']] = row['Name']

# Print the dictionary keys
print(baby_names.keys())
