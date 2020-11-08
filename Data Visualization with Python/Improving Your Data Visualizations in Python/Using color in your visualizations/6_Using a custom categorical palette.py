# Filter our data to Jan 2013
pollution_jan13 = pollution.query('year  ==  2013 & month  ==  1')

# Color lines by the city and use custom ColorBrewer palette
sns.lineplot(x = "day", 
             y = "CO", 
             palette = "Set2",
             hue = "city", 
             linewidth = 3,
             data = pollution_jan13)
plt.show()