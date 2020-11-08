def rank(series):
    # Calculate the mean of the input series
    mean = np.mean(series)
    # Return the mean and its rank as a list
    if mean > 90:
        return [mean, 'high']
    if mean > 60:
        return [mean, 'medium']
    return [mean, 'low']

# Insert the output of rank() into new columns of scores
cols = ['math score', 'reading score', 'writing score']
scores[['mean', 'rank']] = scores[cols].apply(rank, axis=1,
                                              result_type='expand')
print(scores[['mean', 'rank']].head())
