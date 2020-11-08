# Call time.time()
t0 = time.time()

# Read 'WDI.csv' into df
df = pd.read_csv('WDI.csv')

# Group df by region: result
result = by_region(df)

# Call time.time()
t1 = time.time()

# Print the execution time
print((t1-t0)*1000)

# Time the execution of just by_region with Pandas and print in milliseconds
df = pd.read_csv('WDI.csv')
t0 = time.time()
result = by_region(df)
t1 = time.time()
print((t1-t0)*1000)

# Time the execution of dd.read_csv and by_region together with 'WDI.csv' and print in milliseconds
t0 = time.time()
df = dd.read_csv('WDI.csv')
result = by_region(df)
t1 = time.time()
print((t1-t0)*1000)
