import spacy
import numpy as np

sentences = [' i want to fly from boston at 838 am and arrive in denver at 1110 in the morning',
 ' what flights are available from pittsburgh to baltimore on thursday morning',
 ' what is the arrival time in san francisco for the 755 am flight leaving washington',
 ' cheapest airfare from tacoma to orlando',
 ' round trip fares from pittsburgh to philadelphia under 1000 dollars',
 ' i need a flight tomorrow from columbus to minneapolis',
 ' what kind of aircraft is used on a flight from cleveland to dallas',
 ' show me the flights from pittsburgh to los angeles on thursday',
 ' all flights from boston to washington',
 ' what kind of ground transportation is available in denver',
 ' show me the flights from dallas to san francisco',
 ' show me the flights from san diego to newark by way of houston',
 ' what is the cheapest flight from boston to bwi',
 ' all flights to baltimore after 6 pm',
 ' show me the first class fares from boston to denver',
 ' show me the ground transportation in denver',
 ' all flights from denver to pittsburgh leaving after 6 pm and before 7 pm',
 ' i need information on flights for tuesday leaving baltimore for dallas dallas to boston and boston to baltimore',
 ' please give me the flights from boston to pittsburgh on thursday of next week',
 ' i would like to fly from denver to pittsburgh on united airlines',
 ' show me the flights from san diego to newark',
 ' please list all first class flights on united from denver to baltimore',
 ' what kinds of planes are used by american airlines',
 " i'd like to have some information on a ticket from denver to pittsburgh and atlanta",
 " i'd like to book a flight from atlanta to denver",
 ' which airline serves denver pittsburgh and atlanta',
 " show me all flights from boston to pittsburgh on wednesday of next week which leave boston after 2 o'clock pm",
 ' atlanta ground transportation',
 ' i also need service from dallas to boston arriving by noon',
 ' show me the cheapest round trip fare from baltimore to dallas']

labels = ['atis_flight',
 'atis_flight',
 'atis_flight_time',
 'atis_airfare',
 'atis_airfare',
 'atis_flight',
 'atis_aircraft',
 'atis_flight',
 'atis_flight',
 'atis_ground_service',
 'atis_flight',
 'atis_flight',
 'atis_flight',
 'atis_flight',
 'atis_airfare',
 'atis_ground_service',
 'atis_flight',
 'atis_flight',
 'atis_flight',
 'atis_flight',
 'atis_flight',
 'atis_flight',
 'atis_aircraft',
 'atis_airfare',
 'atis_flight',
 'atis_airline',
 'atis_flight',
 'atis_ground_service',
 'atis_flight',
 'atis_airfare']

# Load the spacy model: nlp
nlp = spacy.load("en_core_web_sm")

# Calculate the length of sentences
n_sentences = len(sentences)

# Calculate the dimensionality of nlp
embedding_dim = nlp.vocab.vectors_length

# Initialize the array with zeros: X
X = np.zeros((n_sentences, embedding_dim))

# Iterate over the sentences
for idx, sentence in enumerate(sentences):
    # Pass each each sentence to the nlp object to create a document
    doc = nlp(sentence)
    # Save the document's .vector attribute to the corresponding row in X
    X[idx, :] = doc.vector