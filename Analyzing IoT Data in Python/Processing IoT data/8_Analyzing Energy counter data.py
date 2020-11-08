# Get difference between values
df_diff = df.diff() 

# Plot the DataFrame
df_diff.plot()
plt.show()


# Resample df to 30 minutes
df_res = df.resample('30min').max()

# Get difference between values
df_diff = df_res.diff()

# Get the percent changed
df_pct = df_diff.pct_change()

# Plot the DataFrame
df_pct.plot()
plt.show()