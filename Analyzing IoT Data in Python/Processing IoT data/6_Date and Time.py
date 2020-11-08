# Convert the timestamp
df.ts = pd.to_datetime(df.ts)

# Print datatypes and first observations
print(df.dtypes)
print(df.head())


# Convert the timestamp
df["ts"] = pd.to_datetime(df.ts,unit='ms' )

# Print datatypes and first observations
print(df.dtypes)
print(df.head())
