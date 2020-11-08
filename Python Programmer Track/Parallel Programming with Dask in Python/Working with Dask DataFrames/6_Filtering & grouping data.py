# Filter rows where payment_type == 1: credit
credit = df.loc[df['payment_type'] == 1]

# Group by 'hour' column: hourly
hourly = credit.groupby('hour')

# Aggregate mean 'tip_fraction' and print its data type
result = hourly['tip_fraction'].mean()
print(type(result))
