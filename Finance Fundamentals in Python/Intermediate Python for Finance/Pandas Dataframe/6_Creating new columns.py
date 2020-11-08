# Use the list pcesv to create the column PCESV
pce['PCESV'] = pcesv

# Use the DataFrame pcnd to create the column PCND
pce['PCND'] = pcnd

# Create column for PCDG using Pandas read_csv
pce['PCDG'] = pd.read_csv('pcdg.csv', index_col='DATE')

# Create a column PCE by adding values from other columns
pce['PCE'] = pce['PCDG'] + pce['PCESV'] + pce['PCND']
pce.head()
