# Define the split day
limit_day = "2018-10-27"

# Split the data
train_env = environment[:limit_day]
test_env = environment[limit_day:]

# Print start and end dates
print(show_start_end(train_env))
print(show_start_end(test_env))

# Split the data into X and y
X_train = train_env.drop('target', axis=1)
y_train = train_env['target']
X_test = test_env.drop('target', axis=1)
y_test = test_env['target']