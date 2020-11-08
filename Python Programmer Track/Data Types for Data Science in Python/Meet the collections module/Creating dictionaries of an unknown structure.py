# Create an empty dictionary: ridership
ridership = {}

# Iterate over the entries
for date, stop, riders in entries:
    # Check to see if date is already in the ridership dictionary
    if date not in ridership:
        # Create an empty list for any missing date
        ridership[date] = list()
    # Append the stop and riders as a tuple to the date keys list
    ridership[date].append((stop, riders))

# Print the ridership for '03/09/2016'
print(ridership['03/09/2016'])
