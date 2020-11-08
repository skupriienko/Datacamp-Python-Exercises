# Import time
import time

# Call da.from_array() with arr: energy_dask4
energy_dask4 = da.from_array(energy, chunks=8784)

# Print the time to compute standard deviation
t_start = time.time()
std_4 = energy_dask4.std().compute()
t_end = time.time()
print((t_end - t_start) * 1.0e3)


# Call da.from_array() with arr: energy_dask8
energy_dask8 = da.from_array(energy, chunks=energy.shape[0]//8)

# Print the time to compute standard deviation
t_start = time.time()
std_8 = energy_dask8.std().compute()
t_end = time.time()
print((t_end - t_start) * 1.0e3)
