from operator import itemgetter


def all_laureates(prize):
    # sort the laureates by surname
    sorted_laureates = sorted(prize["laureates"], key=itemgetter("surname"))

    # extract surnames
    surnames = [laureate["surname"] for laureate in sorted_laureates]

    # concatenate surnames separated with " and "
    all_names = " and ".join(surnames)

    return all_names


# find physics prizes, project year and name, and sort by year
docs = db.prizes.find(
    filter={"category": "physics"},
    projection=["year", "laureates.firstname", "laureates.surname"],
    sort=[("year", 1)])

# print the year and laureate names (from all_laureates)
for doc in docs:
    print("{year}: {names}".format(year=doc['year'], names=all_laureates(doc)))