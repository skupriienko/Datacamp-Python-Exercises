# Make bee swarm plot
_ = sns.swarmplot('ID', 'impact_force', data=df)

# Label axes
_ = plt.xlabel('frog')
_ = plt.ylabel('impact force (N)')

# Show the plot
plt.show()
