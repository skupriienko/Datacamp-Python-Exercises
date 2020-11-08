import spacy

nlp = spacy.load('en_core_web_sm')

TEXTS = ['McDonalds is my favorite restaurant.',
 'Here I thought @McDonalds only had precooked burgers but it seems they only have not cooked ones?? I have no time to get sick..',
 'People really still eat McDonalds :(',
 'The McDonalds in Spain has chicken wings. My heart is so happy ',
 '@McDonalds Please bring back the most delicious fast food sandwich of all times!!....The Arch Deluxe :P',
 'please hurry and open. I WANT A #McRib SANDWICH SO BAD! :D',
 'This morning i made a terrible decision by gettin mcdonalds and now my stomach is payin for it']

# Process the texts and print the adjectives
for doc in nlp.pipe(TEXTS):
    print([token.text for token in doc if token.pos_ == 'ADJ'])

# Process the texts and print the entities
docs =  list(nlp.pipe(TEXTS))
entities = [doc.ents for doc in docs]
print(*entities)

people = ['David Bowie', 'Angela Merkel', 'Lady Gaga']

# Create a list of patterns for the PhraseMatcher
patterns = list(nlp.pipe(people))