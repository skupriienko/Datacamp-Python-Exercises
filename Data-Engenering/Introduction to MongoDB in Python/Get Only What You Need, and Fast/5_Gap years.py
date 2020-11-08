# original categories from 1901
original_categories = db.prizes.distinct("category", {"year": "1901"})
print(original_categories)

# project year and category, and sort
docs = db.prizes.find(
        filter={},
        projection={"year":1, "category":1, "_id":0},
        sort=[("year", -1), ("category", 1)]
)

#print the documents
for doc in docs:
  print(doc)