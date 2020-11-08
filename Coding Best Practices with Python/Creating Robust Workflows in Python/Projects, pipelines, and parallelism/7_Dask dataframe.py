import dask.dataframe as dd

# Read in a csv file using a dask.dataframe method
df = dd.read_csv("diabetes.csv")

df["bin_age"] = (df.age > 0).astype(int)

# Compute the columns means in the two age groups
print(df.groupby("bin_age").mean().compute())
