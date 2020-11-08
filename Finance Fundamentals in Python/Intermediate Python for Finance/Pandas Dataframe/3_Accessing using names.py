# Select the Balance for October 2nd
print(ledger.loc['2020-10-02','Balance'])

# Select the Balance for October 3rd
print(ledger.loc['2020-10-03','Balance'])


# Cash and Securities for October 3rd
print(ledger.loc['2020-10-03', ['Cash', 'Securities']])

# Balance for October 1st and 3rd
print(ledger.loc[['2020-10-01', '2020-10-03'], 'Balance'])

# All columns for October 1st
print(ledger.loc['2020-10-01', :])

# Balance for all dates
print(ledger.loc[:, 'Balance'])
