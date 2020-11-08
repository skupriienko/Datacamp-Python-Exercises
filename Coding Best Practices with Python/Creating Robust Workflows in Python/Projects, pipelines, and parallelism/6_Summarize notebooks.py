import scrapbook as sb

# Assign the scrapbook notebook object to nb
nb = sb.read_notebook("rf_diabetes.ipynb")

# Create a dataframe of scraps (recorded values)
scrap_df = nb.scrap_dataframe
print(scrap_df)
