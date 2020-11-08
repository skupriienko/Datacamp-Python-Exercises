# Import the language detection package
import langdetect

# Loop over the rows of the dataset and append
languages = []
for i in range(len(non_english_reviews)):
    languages.append(langdetect.detect_langs(non_english_reviews.iloc[i, 1]))

# Clean the list by splitting
languages = [str(lang).split(':')[0][1:] for lang in languages]
# Assign the list to a new feature
non_english_reviews['language'] = languages

# Select the Spanish ones
non_english_reviews = non_english_reviews[non_english_reviews.language == 'es']

# Import the required packages
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize

# Import the Spanish SnowballStemmer
SpanishStemmer = SnowballStemmer("spanish")

# Create a list of tokens
tokens = [word_tokenize(review) for review in non_english_reviews.review]
# Stem the list of tokens
stemmed_tokens = [[SpanishStemmer.stem(word) for word in token] for token in tokens]

# Print the first item of the stemmed tokenss
stemmed_tokens[0]