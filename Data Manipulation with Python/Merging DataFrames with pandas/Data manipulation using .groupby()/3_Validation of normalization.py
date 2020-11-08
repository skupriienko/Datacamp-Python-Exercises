zscore = lambda x: (x - x.mean()) / x.std()

# Apply the transformation
poker_trans = poker_grouped.transform(zscore)

# Re-group the grouped object
poker_regrouped = poker_trans.groupby(poker_hands['Class'])

# Print each group's means and standard deviation
print(np.round(poker_regrouped.mean(), 3))
print(poker_regrouped.std())
