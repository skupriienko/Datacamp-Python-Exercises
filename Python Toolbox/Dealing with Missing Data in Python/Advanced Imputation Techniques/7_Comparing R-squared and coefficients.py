# Store the Adj. R-squared scores of the linear models
r_squared = pd.DataFrame({'Complete Case': lm.rsquared_adj, 
                          'Mean Imputation': lm_mean.rsquared_adj, 
                          'KNN Imputation': lm_KNN.rsquared_adj, 
                          'MICE Imputation': lm_MICE.rsquared_adj}, 
                         index=['Adj. R-squared'])

print(r_squared)

# Store the coefficients of the linear models
coeff = pd.DataFrame({'Complete Case': lm.params,
                      'Mean Imputation': lm_mean.params,
                      'KNN Imputation': lm_KNN.params,
                      'MICE Imputation': lm_MICE.params})

print(coeff)

r_squares = {'Mean Imputation': lm_mean.rsquared_adj,
             'KNN Imputation': lm_KNN.rsquared_adj,
             'MICE Imputation': lm_MICE.rsquared_adj}

# Select best R-squared
best_imputation = max(r_squares, key=r_squares.get)

print("The best imputation technique is: ", best_imputation)