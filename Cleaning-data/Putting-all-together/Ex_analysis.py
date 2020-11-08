# Since 1800, life expectancy around the globe has been steadily going up. 
# You would expect the Gapminder data to confirm this.

# The DataFrame g1800s has been pre-loaded.
# In [3]: !ls
# figure.svg  g1800.csv  g1900.csv  g2000.csv

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Create the scatter plot
g1800s.plot(kind='scatter', x='1800', y='1899')

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()
