# Loop through buys
for buy in buys:
    print('Buying ' + buy['symbol'])
    new_balance = balance - buy['total_cost']
    balance = new_balance

print(balance)

for buy in buys:
    print('Buying ' + buy['symbol'])
    new_balance = balance - buy['total_cost']
    if new_balance < 0:
        print('Unable to finish buys')
        break
    balance = new_balance

print(balance)
