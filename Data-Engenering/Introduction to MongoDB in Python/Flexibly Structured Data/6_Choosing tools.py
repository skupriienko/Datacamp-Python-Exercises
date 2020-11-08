# Filter for laureates born in Austria with non-Austria prize affiliation
criteria = {'bornCountry': 'Austria',
              'prizes.affiliations.country': {"$ne": 'Austria'}}

# Count the number of such laureates
count = db.laureates.count_documents(criteria)
print(count)