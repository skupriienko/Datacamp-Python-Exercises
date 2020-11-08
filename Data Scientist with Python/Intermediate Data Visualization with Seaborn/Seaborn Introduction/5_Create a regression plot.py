# Create a regression plot of premiums vs. insurance_losses
sns.regplot(x="insurance_losses", y="premiums", data=df)



# Display the plot
plt.show()

# Create an lmplot of premiums vs. insurance_losses
sns.lmplot(y="premiums", x="insurance_losses", data=df)



# Display the second plot
plt.show()
