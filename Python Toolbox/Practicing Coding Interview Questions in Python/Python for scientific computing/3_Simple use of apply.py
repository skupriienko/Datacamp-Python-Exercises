def prevalence(series):
    vals = list(series)
    # Create a tuple list with unique items and their counts
    itms = [(x, vals.count(x)) for x in set(series)]
    # Extract a tuple with the highest counts using reduce()
    res = reduce(lambda x, y: x if x[1] > y[1] else y, itms)
    # Return the item with the highest counts
    return res[0]

# Apply the prevalence function on the scores DataFrame
result = scores[groups_to_consider].apply(prevalence)
print(result)
