TEXTS = ['How to preorder the iPhone X',
 'iPhone X is coming',
 'Should I pay $1,000 for the iPhone X?',
 'The iPhone 8 reviews are here',
 'Your iPhone goes up to 11 today',
 'I need a new phone! Any tips?']

import spacy

nlp = spacy.load('en_core_web_sm')

# Import the Matcher and initialize it with the shared vocabulary
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)
from spacy.tokens import Doc

# Two tokens whose lowercase forms match 'iphone' and 'x'
pattern1 = [{'LOWER': 'iphone'}, {'LOWER': 'x'}]

# Token whose lowercase form matches 'iphone' and an optional digit
pattern2 = [{'LOWER': 'iphone'}, {'IS_DIGIT': True, 'OP': '?'}]

# Add patterns to the matcher
matcher.add('GADGET', None, pattern1, pattern2)

# Create a Doc object for each text in TEXTS
for doc in nlp.pipe(TEXTS):
    # Find the matches in the doc
    matches = matcher(doc)

    # Get a list of (start, end, label) tuples of matches in the text
    entities = [(start, end, 'GADGET') for matcher_id, start, end in matches]
    print(doc.text, entities)

TRAINING_DATA = []

# Create a Doc object for each text in TEXTS
for doc in nlp.pipe(TEXTS):
    # Match on the doc and create a list of matched spans
    spans = [doc[start:end] for match_id, start, end in matcher(doc)]
    # Get (start character, end character, label) tuples of matches
    entities = [(span.start_char, span.end_char, 'GADGET') for span in spans]

    # Format the matches as a (doc.text, entities) tuple
    training_example = (doc.text, {'entities': entities})
    # Append the example to the training data
    TRAINING_DATA.append(training_example)

print(*TRAINING_DATA, sep='\n')    