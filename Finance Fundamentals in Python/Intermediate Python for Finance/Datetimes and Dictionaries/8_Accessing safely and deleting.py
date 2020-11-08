# Get day eight weeks in future
future_closing_price_date = closing_price_date + timedelta(weeks=8)

# Safely get value for the future date or the string 'Missing'
print(alphabet_hist.get(future_closing_price_date, 'Missing'))

# Print with key
print(alphabet_hist)

# Remove entry
del(alphabet_hist[closing_price_date])

# Print with key deleted
print(alphabet_hist)
