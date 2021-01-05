# Compute an array of velocities as the slope between each point
diff_distances = np.diff(distances)
diff_times = np.diff(times)
velocities = diff_distances / diff_times

# Chracterize the center and spread of the velocities
v_avg = np.mean(velocities)
v_max = np.max(velocities)
v_min = np.min(velocities)
v_range = np.mean(v_max) - np.mean(v_min)

# Plot the distribution of velocities
fig = plot_velocity_timeseries(times[1:], velocities)