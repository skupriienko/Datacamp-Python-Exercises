# Stack with the list of dask arrays: by_year
by_year = da.stack(monthly, axis=0)

# Print the shape of the stacked arrays
print(by_year.shape)

# Read the climatology data: climatology
dset = h5py.File('tmax.climate.hdf5')
climatology = da.from_array(dset['/tmax'], chunks=(1,444,922))

# Reshape the climatology data to be compatible with months
climatology.reshape((1,12,444,922))
