cols = ["temperature", "humidity", "pressure"]

# Create a line plot
df[cols].plot(title="Environmental data")

# Label X-Axis
plt.xlabel('Time')

# Show plot
plt.show()

cols = ["temperature", "humidity", "pressure"]

# Create a line plot
df[cols].plot(title="Environmental data",
              secondary_y='pressure')

# Label X-Axis
plt.xlabel("Time")

# Show plot
plt.show()