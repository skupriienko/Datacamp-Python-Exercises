# In this exercise, your job is to pivot users so that the focus is on 'visitors', with the columns indexed by 'city' and the rows indexed by 'weekday'.

# Pivot the users DataFrame: visitors_pivot
visitors_pivot = users.pivot(
    index='weekday', columns='city', values='visitors')

# Print the pivoted DataFrame
print(visitors_pivot)
