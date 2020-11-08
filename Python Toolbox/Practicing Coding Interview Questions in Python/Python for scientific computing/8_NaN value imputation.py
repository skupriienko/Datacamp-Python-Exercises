# Define a lambda function that imputes NaN values in series
impute = lambda series: series.fillna(np.mean(series))

# Impute NaNs in the bmi column of imp_globmean
imp_globmean['bmi'] = imp_globmean['bmi'].transform(impute)
print("Global mean = " + str(fheroes['bmi'].mean()) + "\n")

groups = imp_grpmean.groupby(['Publisher', 'Alignment'])

# Impute NaNs in the bmi column of imp_grpmean
imp_grpmean['bmi'] = groups['bmi'].transform(impute)
print(groups['bmi'].mean())
