# Calculate correlation
corr = data.corr()

# Print correlation
print(corr)

# Create a heatmap
sns.heatmap(corr, annot=True)

# Show plot
plt.show()