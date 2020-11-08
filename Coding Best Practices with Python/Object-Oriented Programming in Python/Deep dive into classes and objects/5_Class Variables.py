# Create class: DataShell
class DataShell:

    # Declare a class variable family, and assign value of "DataShell"
    family = "DataShell"

    # Initialize class with self, identifier arguments
    def __init__(self, identifier):

        # Set identifier as instance variable of input argument
        self.identifier = identifier

# Declare variable x with value of 100
x = 100

# Instantiate DataShell passing x as argument: my_data_shell
my_data_shell = DataShell(x)

# Print my_data_shell class variable family
print(my_data_shell.family)
