from langdetect import detect_langs

languages = []

# Loop over the sentences in the list and detect their language
for sentence in range(len(sentences)):
    languages.append(detect_langs(sentences[sentence]))

print('The detected languages are: ', languages)