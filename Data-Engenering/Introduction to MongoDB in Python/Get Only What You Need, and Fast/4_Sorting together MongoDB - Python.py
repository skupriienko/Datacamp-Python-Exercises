from operator import itemgetter


def all_laureates(prize):
    # sort the laureates by surname
    sorted_laureates = sorted(prize['laureates'], key=itemgetter('surname'))

    # extract surnames
    surnames = [laureate['surname'] for laureate in sorted_laureates]

    # concatenate surnames separated with " and "
    all_names = " and ".join(surnames)

    return all_names


# test the function on a sample doc
print(all_laureates(sample_prize))