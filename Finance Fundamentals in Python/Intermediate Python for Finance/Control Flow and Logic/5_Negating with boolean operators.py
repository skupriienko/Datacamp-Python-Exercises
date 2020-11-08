print(closing_prices)

# Assigning True if we need to get the prices
not_prices = not closing_prices

print(not_prices)

# Get prices if market is closed and we don't have prices
get_prices = not (market_closed and not_prices)

print(get_prices)
