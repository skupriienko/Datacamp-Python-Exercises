# Import the Counter object
from collections import Counter

# stations = []

# Print the first ten items from the stations list
print(stations[:10])

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Print the station_count
print(station_count)

# Find the 5 most common elements
print(station_count.most_common(5))
