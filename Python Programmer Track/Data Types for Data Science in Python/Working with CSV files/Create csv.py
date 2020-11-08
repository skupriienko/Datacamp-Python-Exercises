# Import the python CSV module
import csv

# Create a python file object in read mode for the baby_names.csv file: csvfile
csvfile = open('contacts.csv', 'r')

names = {}
# Loop over a csv reader on the file object
for row in csv.reader(csvfile):
    # Print each row
    # print(row)
    # Add the rank and name to the dictionary
    names[row[5]] = row[3]

# Print the dictionary keys
print(names.keys())
