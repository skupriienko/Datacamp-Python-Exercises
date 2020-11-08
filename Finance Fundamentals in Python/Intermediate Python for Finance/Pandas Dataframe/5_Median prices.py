# Get the median of the opening prices
med_open = prices.loc[:, 'OPEN'].median()

# Get the median of the closing prices
med_close = prices.loc[:, 'CLOSE'].median()

if med_open < med_close:
    print("Trending down.")
