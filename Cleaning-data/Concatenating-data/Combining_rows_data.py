# The dataset you'll be working with here relates to NYC Uber data 
# (http://data.beta.nyc/dataset/uber-trip-data-foiled-apr-sep-2014). 
# The original dataset has all the originating Uber pickup locations 
# by time and latitude and longitude. 

# Concatenate uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1, uber2, uber3])

# Print the shape of row_concat
print(row_concat.shape)

# Print the head of row_concat
print(row_concat.head())



