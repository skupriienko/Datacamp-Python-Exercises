# Create class: DataShell
class DataShell:

    # Declare a class variable family, and assign value of "DataShell"
    family = "DataShell"

    # Initialize class with self, identifier arguments
    def __init__(self, identifier):

        # Set identifier as instance variables, assigning value of input arguments
        self.identifier = identifier

# Declare variable x with value of 100
x = 100

# Instantiate DataShell passing x as the argument: my_data_shell
my_data_shell = DataShell(x)

# Print my_data_shell class variable family
print(my_data_shell.family)

# Override the my_data_shell.family value with "NotDataShell"
my_data_shell.family = 'NotDataShell'

# Print my_data_shell class variable family once again
print(my_data_shell.family)
