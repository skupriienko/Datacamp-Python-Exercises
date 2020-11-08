# In this exercise, we have imported pandas as pd and defined 
# a DataFrame df containing top Billboard hits from the 1980s (from Wikipedia - 
# https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_1980s#1980). 
# Each row has the year, artist, song name and the number of weeks at the top. 
# However, this DataFrame has the column labels a, b, c, d. 
# Your job is to use the df.columns attribute to re-assign descriptive column labels.

# Build a list of labels: list_labels
list_labels = list(['year', 'artist', 'song', 'chart weeks'])

# Assign the list of labels to the columns attribute: df.columns
df.columns = list_labels