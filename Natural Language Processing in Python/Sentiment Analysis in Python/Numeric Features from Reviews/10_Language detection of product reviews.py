from langdetect import detect_langs
languages = []

# Loop over the rows of the dataset and append
for row in range(len(non_english_reviews)):
    languages.append(detect_langs(non_english_reviews.iloc[row, 1]))

# Clean the list by splitting
languages = [str(lang).split(':')[0][1:] for lang in languages]

# Assign the list to a new feature
non_english_reviews['language'] = languages

print(non_english_reviews.head())