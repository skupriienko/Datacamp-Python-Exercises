#  Your job is to plot all columns as a multi-line plot, 
# to see the nature of vertical scaling problem. 
# Then, use a list of column names passed into 
# the DataFrame df[column_list] to limit plotting to 
# ust one column, and then just 2 columns of data. 
# When you are finished, you will have created 4 plots.

# Plot all columns (default)
df.plot()
plt.show()

# Plot all columns as subplots
df.plot(subplots=True)
plt.show()

# Plot just the Dew Point data
column_list1 = ['Dew Point (deg F)']
df[column_list1].plot()
plt.show()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['Temperature (deg F)','Dew Point (deg F)']
df[column_list2].plot()
plt.show()
plt.show()