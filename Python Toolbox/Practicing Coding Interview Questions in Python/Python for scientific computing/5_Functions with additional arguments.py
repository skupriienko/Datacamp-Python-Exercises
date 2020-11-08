def rescale(series, low, high):
   # Define the expression to rescale input series
   return series * (high - low)/100 + low

# Rescale the data in cols to lie between 1 and 10
cols = ['math score', 'reading score', 'writing score']
scores[cols] = scores[cols].apply(rescale, args=[1, 10])
print(scores[cols].head())


# Redefine the function to accept keyword arguments
def rescale(series, low=0, high=100):
   return series * (high - low)/100 + low

# Rescale the data in cols to lie between 1 and 10
cols = ['math score', 'reading score', 'writing score']
scores[cols] = scores[cols].apply(rescale, low=1, high=10)
print(scores[cols].head())
