# import all modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

grant_file = 'E:/src/Datacamp/Data Scientist with Python/Intermediate Data Visualization with Seaborn/schoolimprovement2010grants.csv'
# Read in the DataFrame
df = pd.read_csv(grant_file)

print(df.head())
# Display pandas histogram
df['Award_Amount'].plot.hist()
plt.show()

# Clear out the pandas histogram
plt.clf()

# Display a Seaborn distplot
sns.distplot(df['Award_Amount'])
plt.show()

# Clear the distplot
plt.clf()
