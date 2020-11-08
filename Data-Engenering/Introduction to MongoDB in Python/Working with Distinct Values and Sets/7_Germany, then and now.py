from bson.regex import Regex

# Filter for laureates with "Germany" in their "bornCountry" value
criteria = {"bornCountry": Regex("Germany", 0)}
print(set(db.laureates.distinct("bornCountry", criteria)))

from bson.regex import Regex

# Filter for laureates with a "bornCountry" value starting with "Germany"
criteria = {"bornCountry": Regex('^Germany')}
print(set(db.laureates.distinct("bornCountry", criteria)))

from bson.regex import Regex

# Filter for laureates with "Germany" in their "bornCountry" value
criteria = {"bornCountry": Regex("Germany", 0)}
print(set(db.laureates.distinct("bornCountry", criteria)))

from bson.regex import Regex

#Filter for currently-Germany countries of birth. Fill in a string value to be sandwiched between the strings "now" and "$"
criteria = {"bornCountry": Regex("now" + ' Germany\\)' + "$")}
print(set(db.laureates.distinct("bornCountry", criteria)))