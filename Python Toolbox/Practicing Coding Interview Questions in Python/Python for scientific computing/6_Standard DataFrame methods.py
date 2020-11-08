# Load the data from the diabetes.csv file
diabetes = pd.read_csv('diabetes.csv')
print(diabetes.info())

# Calculate the mean glucose level in the entire dataset
print(diabetes['plasma glucose'].mean())

# Group the data according to the diabetes test results
diabetes_grouped = diabetes.groupby('test result')

# Calculate the mean glucose levels per group
print(diabetes_grouped['plasma glucose'].mean())
