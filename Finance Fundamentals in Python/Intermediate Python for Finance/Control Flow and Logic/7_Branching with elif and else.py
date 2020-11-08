# Get the symbol value
symbol = trn['symbol']

# Check if Apple stock
if symbol == 'APPL':
    appl.append(trn)
# Check if Tesla stock
elif symbol == 'TSLA':
    tsla.append(trn)
# Check if Amazon stock
elif symbol == 'AMZN':
    amzn.append(trn)
# Handle other companies
else:
    print(symbol)
