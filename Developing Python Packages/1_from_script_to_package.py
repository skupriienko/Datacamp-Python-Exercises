def count_words(filepath, words_list):

    # Open the text file
    with open(filepath) as file:
        text = file.read()

    words_list = []
    n = 0
    for word in text.split():
        # Count the number of times the words in the list appear
        if word.lower() in ['cat', 'cats']:
            n += 1

    print('Lewis Carroll uses the word "cat" {} times'.format(n))
    
    return n
