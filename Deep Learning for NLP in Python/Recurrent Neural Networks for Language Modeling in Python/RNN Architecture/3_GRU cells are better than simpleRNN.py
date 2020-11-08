# Import the modules
from keras.layers import GRU, Dense

# Print the old and new model summaries
SimpleRNN_model.summary()
gru_model.summary()

# Evaluate the models' performance (ignore the loss value)
_, acc_simpleRNN = SimpleRNN_model.evaluate(X_test, y_test, verbose=0)
_, acc_GRU = gru_model.evaluate(X_test, y_test, verbose=0)

# Print the results
print("SimpleRNN model's accuracy:\t{0}".format(acc_simpleRNN))
print("GRU model's accuracy:\t{0}".format(acc_GRU))