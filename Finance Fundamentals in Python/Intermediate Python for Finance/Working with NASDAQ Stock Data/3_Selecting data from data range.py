# Calculate the mask for one week
mask = (end_date <= alphabet['date']) & (alphabet['date'] <= start_date)

# Use the mask to get the data for one week
df = alphabet[mask]

# Look at result
print(df)
