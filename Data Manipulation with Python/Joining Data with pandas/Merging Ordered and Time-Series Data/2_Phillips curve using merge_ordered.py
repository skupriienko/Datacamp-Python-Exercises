# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = inflation.merge(unemployment, on='date')

# Print inflation_unemploy 
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(kind='scatter', x='unemployment_rate', y='cpi')
plt.show()