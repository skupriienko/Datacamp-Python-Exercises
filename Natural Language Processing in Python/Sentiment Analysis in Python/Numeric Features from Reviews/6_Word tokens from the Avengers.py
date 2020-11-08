# Import the word tokenizing function
from nltk import word_tokenize

avengers = ["Cause if we can't protect the Earth, you can be d*** sure we'll avenge it",
 'There was an idea to bring together a group of remarkable people, to see if we could become something more',
 "These guys come from legend, Captain. They're basically Gods."]
# Tokenize each item in the avengers
tokens_avengers = [word_tokenize(item) for item in avengers]

print(tokens_avengers)