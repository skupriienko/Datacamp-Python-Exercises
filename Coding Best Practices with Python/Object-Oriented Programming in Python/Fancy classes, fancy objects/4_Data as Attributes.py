# Import numpy as np, pandas as pd
import numpy as np
import pandas as pd

# Create class: DataShell
class DataShell:

    # Define initialization method
    def __init__(self, filepath):
        # Set filepath as instance variable
        self.filepath = filepath
        # Set data_as_csv as instance variable
        self.data_as_csv = pd.read_csv(filepath)

# Instantiate DataShell as us_data_shell
us_data_shell = DataShell(us_life_expectancy)

# Print your object's data_as_csv attribute
print(us_data_shell.data_as_csv)
