# Resample dataframe to 1h
df_seas = df.resample('1h').max()

# Run seasonal decompose
decomp = sm.tsa.seasonal_decompose(df_seas)

# Plot the timeseries
plt.title("Temperature")
plt.plot(df_seas["temperature"], label="temperature")

# Plot trend and seasonality
plt.plot(decomp.trend["temperature"], label='trend')
plt.plot(decomp.seasonal["temperature"], label="seasonal")
plt.legend()
plt.show()