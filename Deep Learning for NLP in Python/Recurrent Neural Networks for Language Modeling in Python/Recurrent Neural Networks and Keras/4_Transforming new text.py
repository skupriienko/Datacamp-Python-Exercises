new_text = ['A man either lives life as it happens to him meets it head-on and licks it or he turns his back on it and starts to wither away',
 'To the brave crew and passengers of the Kobayshi Maru sucks to be you',
 'Beware of more powerful weapons They often inflict as much damage to your soul as they do to you enemies',
 'They are merely scars not mortal wounds and you must use them to propel you forward',
 'You cannot explain away a wantonly immoral act because you think that it is connected to some higher purpose']

# Loop through the sentences and get indexes
new_text_split = []
for sentence in new_text:
    sent_split = []
    for wd in sentence.split(' '):
        index = word_to_index.get(wd, 0)
        sent_split.append(index)
    new_text_split.append(sent_split)

# Print the first sentence's indexes
print(new_text_split[0])

# Print the sentence converted using the dictionary
print(' '.join([index_to_word[index] for index in new_text_split[0]]))