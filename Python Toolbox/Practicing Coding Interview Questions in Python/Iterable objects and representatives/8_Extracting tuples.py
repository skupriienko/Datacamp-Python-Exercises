# Create a list of tuples with lengths and longest words
result = [
    (len(item), get_longest_word(item)) for item in wlist
]

# Unzip the result
lengths, words = zip(*result)

for item in zip(wlist, lengths, words):
    print(item)
