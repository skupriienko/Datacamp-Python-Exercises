def my_special_function():
    print('You are running my_special_function()')

    def get_new_func(func):
        def call_func():
            func()
    return call_func

new_func = get_new_func(my_special_function)

# Redefine my_special_function() to just print "hello"
def my_special_function():
    print('hello')

# Delete my_special_function()
del my_special_function


new_func()


# Overwrite `my_special_function` with the new function
my_special_function = get_new_func(my_special_function)

my_special_function()
