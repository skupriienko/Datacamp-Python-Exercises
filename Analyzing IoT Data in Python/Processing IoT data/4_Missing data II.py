# Calculate and print NA count
print(data.isna().sum())

# Resample data
data_res = data.resample("10min").last()

# Calculate and print NA count
print(data_res.isna().sum())

# Plot the dataframe
data_res.plot()

plt.show()