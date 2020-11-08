# Create a Keras model with one hidden Dense layer
model = Sequential()
model.add(Dense(25, input_dim=20, activation='relu', kernel_initializer=he_uniform(seed=42)))
model.add(Dense(1, activation='linear'))

# Compile and fit the model
model.compile(loss='mean_squared_error', optimizer=SGD(lr=0.01, momentum=0.9))
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, verbose=0)

# See Mean Square Error for train and test data
train_mse = model.evaluate(X_train, y_train, verbose=0)
test_mse = model.evaluate(X_test, y_test, verbose=0)

# Print the values of MSE
print('Train: %.3f, Test: %.3f' % (train_mse, test_mse))

# Create a Keras model with one hidden Dense layer
model = Sequential()
model.add(Dense(25, input_dim=20, activation='relu', kernel_initializer=he_uniform(seed=42)))
model.add(Dense(1, activation='linear'))

# Compile and fit the model
model.compile(loss='mean_squared_error', optimizer=SGD(lr=0.01, momentum=0.9, clipvalue=3.0))
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, verbose=0)

# See Mean Square Error for train and test data
train_mse = model.evaluate(X_train, y_train, verbose=0)
test_mse = model.evaluate(X_test, y_test, verbose=0)

# Print the values of MSE
print('Train: %.3f, Test: %.3f' % (train_mse, test_mse))