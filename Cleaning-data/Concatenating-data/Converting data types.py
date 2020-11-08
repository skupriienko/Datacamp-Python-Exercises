# all categorical variables in a DataFrame are of type category reduces memory usage.

# The tips dataset has been loaded into a DataFrame called tips. 
# This data contains information about how much a customer tipped, 
# whether the customer was male or female, a smoker or not, etc.

# Convert the sex column to type 'category'
tips.sex = tips.sex.astype('category')

# Convert the smoker column to type 'category'
tips.smoker = tips.smoker.astype('category')

# Print the info of tips
print(tips.info())

# Working with numeric data

# Convert 'total_bill' to a numeric dtype
tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors='coerce')

# Convert 'tip' to a numeric dtype
tips['tip'] = pd.to_numeric(tips['tip'], errors='coerce')

# Print the info of tips
print(tips.info())
