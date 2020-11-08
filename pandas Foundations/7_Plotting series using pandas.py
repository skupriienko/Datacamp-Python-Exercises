#  We have pre-loaded a pandas DataFrame df which contains 
# the data you need. Your job is to use the DataFrame method df.plot() 
# to visualize the data, and then explore the 
# optional matplotlib input parameters that this .plot() method accepts.

# Create a plot with color='red'
df.plot(color='red')

# Add a title
plt.title('Temperature in Austin')

# Specify the x-axis label
plt.xlabel('Hours since midnight August 1, 2010')

# Specify the y-axis label
plt.ylabel('Temperature (degrees F)')

# Display the plot
plt.show()