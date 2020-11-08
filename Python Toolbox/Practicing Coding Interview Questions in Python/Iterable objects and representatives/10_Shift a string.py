def shift_string(string, shift):
    len_string = len(string)
    # Loop over the indices of a string
    for idx in range(0, len_string):
        # Find which character will correspond to the index.
        yield string[(idx - shift) % len_string]

# Create a generator
gen = shift_string('DataCamp', 3)

# Create a new string using the generator and print it out
string_shifted = ''.join(gen)
print(string_shifted)
