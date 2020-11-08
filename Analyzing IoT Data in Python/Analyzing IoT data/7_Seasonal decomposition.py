# Import modules
import statsmodels.api as sm

# Perform decompositon 
res = sm.tsa.seasonal_decompose(traffic['vehicles'])

# Print the seasonal component
print(res.seasonal.head())

# Plot the result
res.plot()

# Show the plot
plt.show()