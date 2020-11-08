# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
plt.plot(x_vers, y_vers, marker=".", linestyle="none")

# Label the axes
plt.xlabel('Iris versicolor')
plt.ylabel('ECDF')


# Display the plot
plt.show()
