# Calculate mean
data["mean"] = data.temperature.mean()

# Calculate upper and lower limits
data["upper_limit"] = data['mean'] + (data['temperature'].std() * 3)
data["lower_limit"] = data['mean'] - (data['temperature'].std() * 3)

# Plot the dataframe
data.plot()

plt.show()