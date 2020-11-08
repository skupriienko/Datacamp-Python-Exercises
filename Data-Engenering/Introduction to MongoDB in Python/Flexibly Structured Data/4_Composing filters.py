# Create a filter for laureates who died in the USA
criteria = {'diedCountry': 'USA'}

# Save the count of these laureates
count = db.laureates.count_documents(criteria)
print(count)

# Create a filter for laureates who died in the USA but were born in Germany
criteria = {'diedCountry': 'USA',
            'bornCountry': 'Germany'}

# Save the count
count = db.laureates.count_documents(criteria)
print(count)

# Create a filter for Germany-born laureates who died in the USA and with the first name "Albert"
criteria = {'bornCountry': 'Germany',
            'diedCountry': 'USA',
            'firstname': 'Albert'}

# Save the count
count = db.laureates.count_documents(criteria)
print(count)