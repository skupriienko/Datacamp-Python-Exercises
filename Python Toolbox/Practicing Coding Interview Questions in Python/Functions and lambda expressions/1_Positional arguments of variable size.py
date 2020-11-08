# Define the function with an arbitrary number of arguments
def sort_types(*args):
    nums, strings = [], []
    for arg in args:
        # Check if 'arg' is a number and add it to 'nums'
        if isinstance(arg, (int, float)):
            nums.append(arg)
        # Check if 'arg' is a string and add it to 'strings'
        elif isinstance(arg, str):
            strings.append(arg)

    return (nums, strings)

print(sort_types(1.57, 'car', 'hat', 4, 5, 'tree', 0.89))
