TEST_DATA = ['Apple is slowing down the iPhone 8 and iPhone X - how to stop it',
 "I finally understand what the iPhone X 'notch' is for",
 'Everything you need to know about the Samsung Galaxy S9',
 'Looking to compare iPad models? Here’s how the 2018 lineup stacks up',
 'The iPhone 8 and iPhone 8 Plus are smartphones designed, developed, and marketed by Apple',
 'what is the cheapest ipad, especially ipad pro???',
 'Samsung Galaxy is a series of mobile computing devices designed, manufactured and marketed by Samsung Electronics']

import spacy
import random

# Create a blank 'en' model
nlp = spacy.blank('en')

# Create a new entity recognizer and add it to the pipeline
ner = nlp.create_pipe('ner')
nlp.add_pipe(ner)

# Add the label 'GADGET' to the entity recognizer
ner.add_label('GADGET')

# Process each text in TEST_DATA
for doc in nlp.pipe(TEST_DATA):
    # Print the document text and entitites
    print(doc.text)
    print(doc.ents, '\n\n')