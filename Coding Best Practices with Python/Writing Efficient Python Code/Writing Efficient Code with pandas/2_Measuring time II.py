# In the list words, there are random words downloaded from the Internet. We are interested to create another list called listlet in which we only keep the words that start with the letter b. In case you are not familiar with dealing with strings in Python, each string has the .startswith() attribute, which returns a True/False statement whether the string starts with a specific letter/phrase or not.
# Store the time before the execution
start_time = time.time()

# Execute the operation
letlist = [wrd for wrd in words if wrd.startswith('b')]

# Store and print the difference between the start and the current time
total_time_lc = time.time() - start_time
print('Time using list comprehension: {} sec'.format(total_time_lc))

# Store the time before the execution
start_time = time.time()

# Execute the operation
letlist = []
for wrd in words:
    if wrd.startswith('b'):
        letlist.append(wrd)

# Print the difference between the start and the current time
total_time_fl = time.time() - time.time()
print('Time using for loop: {} sec'.format(total_time_fl))

#     Time using list comprehension: 0.04836916923522949 sec
    # Time using for loop: -2.1457672119140625e-06 sec
