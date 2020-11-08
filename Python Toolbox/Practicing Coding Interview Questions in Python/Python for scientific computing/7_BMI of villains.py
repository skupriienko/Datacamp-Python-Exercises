import numpy as np

# Group the data by two factors specified in the context
groups = heroes.groupby(['Publisher', 'Alignment'])

# Filter groups having more than 10 valid bmi observations
fheroes = groups.filter(lambda x: x['bmi'].count() > 10)

# Group the filtered data again by the same factors
fgroups = fheroes.groupby(['Publisher', 'Alignment'])

# Calculate the mean and standard deviation of the BMI index
result = fgroups['bmi'].agg([np.mean, np.std])
print(result)
