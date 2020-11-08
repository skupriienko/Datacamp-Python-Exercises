# Import the LSTM layer
from keras.layers.recurrent import LSTM

# Build model
model = Sequential()
model.add(LSTM(units=128, input_shape=(None, 1), return_sequences=True))
model.add(LSTM(units=128, return_sequences=True))
model.add(LSTM(units=128, return_sequences=False))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Load pre-trained weights
model.load_weights('lstm_stack_model_weights.h5')

print("Loss: %0.04f\nAccuracy: %0.04f" % tuple(model.evaluate(X_test, y_test, verbose=0)))