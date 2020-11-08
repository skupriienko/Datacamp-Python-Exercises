# Call da.from_array():  energy_dask
energy_dask = da.from_array(energy, chunks=8784)

# Print energy_dask.chunks
print(energy_dask.chunks)

# Print Dask array average and then NumPy array average
print(energy_dask.mean().compute())
print(energy.mean())
