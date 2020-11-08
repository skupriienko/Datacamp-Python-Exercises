# Call .str.split(' ') from speeches and assign it to by_word
by_word = speeches.str.split(" ")

# Map the len function over by_word and compute its mean
n_words = by_word.map(len)
avg_words = n_words.mean()

# Print the type of avg_words and value of avg_words.compute()
print(type(avg_words))
print(avg_words.compute())
