# Import missingno as msno
import missingno as msno

# Sort diabetes dataframe on 'Serum Insulin'
sorted_values = diabetes.sort_values('Serum Insulin')

# Visualize the missingness summary of sorted
msno.matrix(sorted_values)

# Display nullity matrix
display("/usr/local/share/datasets/matrix_sorted.png")