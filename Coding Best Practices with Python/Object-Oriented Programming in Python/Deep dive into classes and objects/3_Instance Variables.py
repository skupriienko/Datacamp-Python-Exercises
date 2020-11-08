# Create class: DataShell
class DataShell:

	# Initialize class with self and integerInput arguments
    def __init__(self, integerInput):

		# Set data as instance variable, and assign the value of integerInput
        self.data = integerInput

# Declare variable x with value of 10
x = 10

# Instantiate DataShell passing x as argument: my_data_shell
my_data_shell = DataShell(x)

# Print my_data_shell
print(my_data_shell.data)
