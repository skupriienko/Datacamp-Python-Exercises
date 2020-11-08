import numpy as np

# Calculate the cumulative growth over time
cumulative_growth_forecast =np.cumprod(1+growth_array)

# Forecast the home value over time
home_value_forecast = cumulative_growth_forecast * home_value

# Forecast the home equity value owned over time
cumulative_home_value_owned = home_value_forecast * cumulative_percent_owned

# Plot the home value vs equity accumulated
plt.plot(home_value_forecast, color='red')
plt.plot(cumulative_home_value_owned, color='blue')
plt.legend(handles=[homevalue_plot, homeequity_plot], loc=2)
plt.show()
