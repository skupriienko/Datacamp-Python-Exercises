# Unstack users by 'weekday': byweekday
byweekday = users.unstack('weekday')

# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
print(byweekday.stack('weekday'))

# Unstack users by 'city': bycity
bycity = users.unstack('city')

# Print the bycity DataFrame
print(bycity)

# Stack bycity by 'city' and print it
print(bycity.stack('city'))
