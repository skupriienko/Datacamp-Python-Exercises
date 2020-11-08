# Use find_unique_items() to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

# %timeit find_unique_items(names)
# 2.09 ms +- 322 us per loop (mean +- std. dev. of 7 runs, 1000 loops each)

# %timeit find_unique_items(names)
# 2.09 ms +- 322 us per loop (mean +- std. dev. of 7 runs, 1000 loops each)

# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types)
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n')
