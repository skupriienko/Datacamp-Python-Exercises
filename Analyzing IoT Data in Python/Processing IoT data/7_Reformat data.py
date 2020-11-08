# Replace the timestamp with the parsed timestamp
df['ts'] = pd.to_datetime(df["ts"], unit="ms")
print(df.head())

# Pivot the DataFrame
df2 = pd.pivot_table(df, columns="device", values="val", index="ts")
print(df2.head())

# Resample DataFrame to 1min
df3 = df2.resample('1min').max().dropna()
print(df3.head())

df3.to_csv(TARGET_FILE)