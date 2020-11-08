from pprint import pprint

# Fetch prizes with quarter-share laureate(s)
filter_ = {'laureates.share': '4'}

# Save the list of field names
projection = ['category', 'year', "laureates.motivation"]

# Save a cursor to yield the first five prizes
cursor = db.prizes.find(filter_, projection).sort('year').limit(5)
pprint(list(cursor))