# Create class: DataShell
class DataShell:

	# Initialize class with self argument
    def __init__(self):
        pass

	# Define class method which takes self argument: print_static
    def print_static(self):
        # Print string
        print("You just executed a class method!")

# Instantiate DataShell taking no arguments: my_data_shell
my_data_shell = DataShell()

# Call the print_static method of your newly created object
my_data_shell.print_static()
