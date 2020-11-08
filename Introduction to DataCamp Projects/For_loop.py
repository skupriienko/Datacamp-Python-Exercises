import pandas as pd
import numpy as np
fam = [1.73, 1.68, 1.71, 1.89]
for height in fam:
    print(height)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for i in areas:
    print(i)

fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam):
    print("person " + str(index) + ": " + str(height))

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas):
    print("room " + str(index) + ": " + str(a))


# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas):
    print("room " + str(index + 1) + ": " + str(area))


# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for room, m in house:
    print("the " + str(room) + " is " + str(m) + " sqm")

world = {"afghanistan": 30.55,
         "albania": 2.77,
         "algeria": 39.21}

for key, value in world.items():
    print(key + " -- " + str(value))


# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for st, cp in europe.items():
    print('the capital of ' + st + ' is ' + cp)


# Import numpy as np

# For loop over np_height
for x in np_height:
    print(str(x) + ' inches')

# For loop over np_baseball
for y in np.nditer(np_baseball):
    print(str(y))

# Import cars data
cars = pd.read_csv('cars.csv', index_col=0)

# Iterate over rows of cars
for x, row in cars.iterrows():
    print(x)
    print(row)

# Import cars data
cars = pd.read_csv('cars.csv', index_col=0)

# Adapt for loop
for lab, row in cars.iterrows():
    print(str(lab) + ": " + str(row['cars_per_cap']))

# Import cars data
cars = pd.read_csv('cars.csv', index_col=0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)

# Import cars data
cars = pd.read_csv('cars.csv', index_col=0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)
