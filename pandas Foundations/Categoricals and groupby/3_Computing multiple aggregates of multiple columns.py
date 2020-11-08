# The .agg() method can be used with a tuple or list of aggregations as input. When applying multiple aggregations on multiple columns, the aggregated DataFrame has a multi-level column index. In this exercise, you're going to group passengers on the Titanic by 'pclass' and aggregate the 'age' and 'fare' columns by the functions 'max' and 'median'. You'll then use multi-level selection to find the oldest passenger per class and the median fare price per class. The DataFrame has been pre-loaded as titanic.

import pandas as pd

file = 'titanic.csv'

# Read file into a DataFrame: titanic
titanic = pd.read_csv(file)

print(titanic.head())
# Group titanic by 'pclass': by_class
by_class = titanic.groupby('Pclass')

# # Select 'age' and 'fare'
by_class_sub = by_class[['Age', 'Fare']]

# # Aggregate by_class_sub by 'max' and 'median': aggregated
aggregated = by_class_sub.agg(['max', 'median'])

# # Print the maximum age in each class
print(aggregated.loc[:, ('Age', 'max')])

# # Print the median fare in each class
print(aggregated.loc[:, ('Fare', 'median')])
