def create_math_function(func_name):
    if func_name == 'add':
        def add(a, b):
            return a + b
        return add
    elif func_name == 'subtract':
        # Define the subtract() function
        def subtract(a, b):
            return a - b
        return subtract
    elif func_name == 'multiply':
        # Define the subtract() function
        def multiply(a, b):
            return a * b
        return multiply

    else:
        print("I don't know that one")

add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))

multiply = create_math_function('multiply')
print('5 * 2 = {}'.format(multiply(5, 2)))
