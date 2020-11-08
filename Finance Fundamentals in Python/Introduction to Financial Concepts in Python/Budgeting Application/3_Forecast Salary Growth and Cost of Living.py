import numpy as np

# Create monthly forecasts up to 15 years from now
forecast_months = 12*15

# Set your annual salary growth rate
annual_salary_growth = 0.05

# Calculate your equivalent monthly salary growth rate
monthly_salary_growth = (1 + annual_salary_growth)** (1 / 12) - 1

# Forecast the cumulative growth of your salary
cumulative_salary_growth_forecast = np.cumprod(np.repeat(1 + monthly_salary_growth, forecast_months))

# Calculate the actual salary forecast
salary_forecast = cumulative_salary_growth_forecast * monthly_takehome_salary

# Plot the forecasted salary
plt.plot(salary_forecast, color='blue')
plt.show()
