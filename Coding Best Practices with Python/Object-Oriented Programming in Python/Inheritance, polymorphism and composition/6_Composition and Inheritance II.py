# Define abstract class DataShell
class DataShell:
    family = 'DataShell'
    def __init__(self, name, filepath):
        self.name = name
        self.filepath = filepath

# Define class CsvDataShell
class CsvDataShell(DataShell):
    def __init__(self, name, filepath):
        self.data = pd.read_csv(filepath)
        self.stats = self.data.describe()

# Define class TsvDataShell
class TsvDataShell(DataShell):
    # Initialization method with arguments self, name, filepath
    def __init__(self, name, filepath):
        # Instance variable data
        self.data = pd.read_table(filepath)
        # Instance variable stats
        self.stats = self.data.describe()

# Instantiate CsvDataShell as us_data_shell, print us_data_shell.stats
us_data_shell = CsvDataShell("US", us_life_expectancy)
print(us_data_shell.stats)

# Instantiate TsvDataShell as france_data_shell, print france_data_shell.stats
france_data_shell = TsvDataShell("France", france_life_expectancy)
print(france_data_shell.stats)
