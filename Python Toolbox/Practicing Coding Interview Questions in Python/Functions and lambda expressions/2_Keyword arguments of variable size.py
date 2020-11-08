# Define the function with an arbitrary number of arguments
def key_types(**kwargs):
    dict_type = dict()
    # Iterate over key value pairs
    for key, value in kwargs.items():
        # Update a list associated with a key
        if type(key) in dict_type:
            dict_type[key].append(key)
        else:
            dict_type[value] = [value]

    return dict_type

res = key_types(a=1, b=2, c=(1, 2), d=3.1, e=4.2)
print(res)
