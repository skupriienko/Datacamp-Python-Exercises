# You'll return to the Ebola dataset (https://data.humdata.org/dataset/ebola-cases-2014) 
# you worked with briefly in the last chapter. 
# It has been pre-loaded into a DataFrame called ebola_melt

# Combining columns of data

# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt, status_country], axis=1)

# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the head of ebola_tidy
print(ebola_tidy.head())
