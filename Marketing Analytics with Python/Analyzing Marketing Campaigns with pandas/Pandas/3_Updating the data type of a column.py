# Check the data type of is_retained
print(marketing['is_retained'].dtypes)

# Convert is_retained to a boolean
marketing['is_retained'] = marketing['is_retained'].astype('bool')

# Check the data type of is_retained, again
print(marketing['is_retained'].dtypes)