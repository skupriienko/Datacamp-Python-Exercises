# Call db.read_text with congress/bills*.json: bills_text
bills_text = db.read_text('congress/bills*.json')

# Map the json.loads function over all elements: bills_dicts
bills_dicts = bills_text.map(json.loads)

# Extract the first element with .take(1) and index to the first position: first_bill
first_bill = bills_dicts.take(1)[0]

# Print the keys of first_bill
print(first_bill.keys())
