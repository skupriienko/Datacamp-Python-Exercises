texts = ['So if a photon is directed through a plane with two slits in it and either slit is observed it will not go through both slits. If it’s unobserved it will, however, if it’s observed after it’s left the plane but before it hits its target, it will not have gone through both slits.'
 'Hello, female children. Allow me to inspire you with a story about a great female scientist. Polish-born, French-educated Madame Curie. Co-discoverer of radioactivity, she was a hero of science, until her hair fell out, her vomit and stool became filled with blood, and she was poisoned to death by her own discovery. With a little hard work, I see no reason why that can’t happen to any of you. Are we done? Can we go?']

# Import relevant classes/functions
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# Build the dictionary of indexes
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)

# Change texts into sequence of indexes
texts_numeric = tokenizer.texts_to_sequences(texts)
print("Number of words in the sample texts: ({0}, {1})".format(len(texts_numeric[0]), len(texts_numeric[1])))

# Pad the sequences
texts_pad = pad_sequences(texts_numeric, 60)
print("Now the texts have fixed length: 60. Let's see the first one: \n{0}".format(texts_pad[0]))

