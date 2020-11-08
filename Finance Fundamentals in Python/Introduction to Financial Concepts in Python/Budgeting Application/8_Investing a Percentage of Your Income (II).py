import numpy as np

# Loop through each forecast period
for i in range(forecast_months):

    # Find the previous investment deposit amount
    if i == 0:
        previous_investment = 0
    else:
        previous_investment = investment_portfolio[i-1]

    # Calculate the value of your previous investments, which have grown
    previous_investment_growth = previous_investment*(1 + investment_rate_monthly)

    # Add your new deposit to your investment portfolio
    investment_portfolio[i] =  previous_investment_growth + investment_deposit_forecast[i]

    # Calculate your net worth at each point in time
    net_worth[i] = investment_portfolio[i] + cumulative_savings_new[i]

# Plot your forecasted cumulative savings vs investments and net worth
plot_investments(investment_portfolio, cumulative_savings_new, net_worth)
