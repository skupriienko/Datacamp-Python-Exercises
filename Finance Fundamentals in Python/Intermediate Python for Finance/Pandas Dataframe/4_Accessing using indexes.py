# Cell first row, Price column
print(positions.iloc[0, 3])

# Cell last row, Symbol column
print(positions.iloc[2, 0])

# Oldest two purchase dates
print(positions.iloc[0:2, 1])

# Newest purchase and quantity
print(positions.iloc[2, 1:3])

# Set 2020 quantity
positions.iloc[2,2] = 15

# Set Quantity
positions.iloc[:, 2] = 0
