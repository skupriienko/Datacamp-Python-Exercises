# Subset prices from stock_array_transposed
prices = stock_array_transposed[:, 0]
print(prices)

# Subset earnings from stock_array_transposed
earnings = stock_array_transposed[:, 1]
print(earnings)

# Subset the price and earning for first company
company_1 = stock_array_transposed[0,:]
print(company_1)
