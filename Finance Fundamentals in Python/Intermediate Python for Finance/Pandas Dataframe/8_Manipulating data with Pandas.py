# Combine the source DataFrames into one
gdp = pd.concat([ge, gpdi, ne, pce], axis=1)

# Add the columns and create a new column with the result
gdp['GDP'] = gdp.apply(np.sum, axis=1)
