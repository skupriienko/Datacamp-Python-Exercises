# Save a filter for laureates born in the USA, Canada, or Mexico
criteria = { 'bornCountry':
                { "$in": ['USA', 'Canada', 'Mexico']}
             }

# Count them and save the count
count = db.laureates.count_documents(criteria)
print(count)

# Save a filter for laureates who died in the USA and were not born there
criteria = { 'diedCountry': 'USA',
               'bornCountry': { "$ne": 'USA'},
             }

# Count them
count = db.laureates.count_documents(criteria)
print(count)