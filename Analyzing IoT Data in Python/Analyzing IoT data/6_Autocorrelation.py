# Plot traffic dataset
traffic[:"2018-11-10"].plot()

# Show plot
plt.show()

# Import tsaplots
from statsmodels.graphics import tsaplots

# Plot autocorrelation
tsaplots.plot_acf(traffic.vehicles, lags=50)

# Show the plot
plt.show()