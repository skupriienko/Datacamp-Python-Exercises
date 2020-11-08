# # Load the 'de_core_news_sm' model – spaCy is already imported
# nlp = spacy.load('de_core_news_sm')
#
# text = "Als erstes Unternehmen der Börsengeschichte hat Apple einen Marktwert von einer Billion US-Dollar erreicht"
#
# # Process the text
# doc = nlp(text)
#
# # Print the document text
# print(doc.text)

import spacy
# Load the small English model – spaCy is already imported
nlp = spacy.load('en_core_web_sm')

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Process the text
doc = nlp(text)

# Print the document text
print(doc.text)