TRAINING_DATA = [('How to preorder the iPhone X', {'entities': [(20, 28, 'GADGET')]}),
 ('iPhone X is coming', {'entities': [(0, 8, 'GADGET')]}),
 ('Should I pay $1,000 for the iPhone X?', {'entities': [(28, 36, 'GADGET')]}),
 ('The iPhone 8 reviews are here', {'entities': [(4, 12, 'GADGET')]}),
 ('Your iPhone goes up to 11 today', {'entities': [(5, 11, 'GADGET')]}),
 ('I need a new phone! Any tips?', {'entities': []})]

import spacy
import random

# Create a blank 'en' model
nlp = spacy.blank('en')

# Create a new entity recognizer and add it to the pipeline
ner = nlp.create_pipe('ner')
nlp.add_pipe(ner)

# Add the label 'GADGET' to the entity recognizer
ner.add_label('GADGET')

# Start the training
nlp.begin_training()

# Loop for 10 iterations
for itn in range(10):
    # Shuffle the training data
    random.shuffle(TRAINING_DATA)
    losses = {}

    # Batch the examples and iterate over them
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]

        # Update the model
        nlp.update(texts, annotations, losses=losses)
        print(losses)