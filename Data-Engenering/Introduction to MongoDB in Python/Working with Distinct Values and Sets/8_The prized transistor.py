from bson.regex import Regex

# Save a filter for laureates with prize motivation values containing "transistor" as a substring
criteria = {"prizes.motivation": Regex("transistor")}

# Save the field names corresponding to a laureate's first name and last name
first, last = "firstname", "surname"
print([(laureate[first], laureate[last]) for laureate in db.laureates.find(criteria)])