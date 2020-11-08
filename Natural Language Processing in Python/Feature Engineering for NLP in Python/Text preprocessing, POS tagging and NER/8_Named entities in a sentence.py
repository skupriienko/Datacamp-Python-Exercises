# Load the required model
nlp = spacy.load('en_core_web_sm')

# Create a Doc instance
text = 'Sundar Pichai is the CEO of Google. Its headquarters is in Mountain View.'
doc = nlp(text)

# Print all named entities and their labels
for ent in doc.ents:
    print(ent.text, ent.label_)