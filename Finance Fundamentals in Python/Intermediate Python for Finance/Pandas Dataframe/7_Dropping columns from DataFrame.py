# Print the current columns of the DataFrame pce
print(pce.columns)

# Create a new DataFrame with only PCE column
new_pce = pce.drop(columns=columns_to_drop)
# Print the columns of the new DataFrame
print(new_pce.columns)

# Drop the columns in_place in the original DataFrame
pce.drop(columns=columns_to_drop, inplace=True)

# Print the columns of the DataFrame pce
print(pce.columns)
