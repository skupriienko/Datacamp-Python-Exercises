sheldon_quotes = ["You're afraid of insects and women, Ladybugs must render you catatonic.",
 'Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.',
 'For example, I cry because others are stupid, and that makes me sad.',
 "I'm not insane, my mother had me tested.",
 'Two days later, Penny moved in and so much blood rushed to your genitals, your brain became a ghost town.',
 "Amy's birthday present will be my genitals.",
 '(3 knocks) Penny! (3 knocks) Penny! (3 knocks) Penny!',
 'Thankfully all the things my girlfriend used to do can be taken care of with my right hand.',
 'I would have been here sooner but the bus kept stopping for other people to get on it.',
 'Oh gravity, thou art a heartless bitch.',
 'I am aware of the way humans usually reproduce which is messy, unsanitary and based on living next to you for three years, involves loud and unnecessary appeals to a deity.',
 'Well, today we tried masturbating for money.',
 'I think that you have as much of a chance of having a sexual relationship with Penny as the Hubble telescope does of discovering at the center of every black hole is a little man with a flashlight searching for a circuit breaker.',
 "Well, well, well, if it isn't Wil Wheaton! The Green Goblin to my Spider-Man, the Pope Paul V to my Galileo, the Internet Explorer to my Firefox.",
 "What computer do you have? And please don't say a white one.",
 "She calls me moon-pie because I'm nummy-nummy and she could just eat me up.",
 'Ah, memory impairment; the free prize at the bottom of every vodka bottle.']

# Transform the list of sentences into a list of words
all_words = ' '.join(sheldon_quotes).split(' ')

# Get number of unique words
unique_words = list(set(all_words))

# Dictionary of indexes as keys and words as values
index_to_word = {i:wd for i, wd in enumerate(sorted(unique_words))}

print(index_to_word)

# Dictionary of words as keys and indexes as values
word_to_index = {wd:i for i, wd in enumerate(sorted(unique_words))}

print(word_to_index)