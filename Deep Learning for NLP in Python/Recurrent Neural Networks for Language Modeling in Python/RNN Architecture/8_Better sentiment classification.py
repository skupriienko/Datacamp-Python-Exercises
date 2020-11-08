# Build and compile the model
model = Sequential()
model.add(Embedding(vocabulary_size, wordvec_dim, trainable=True, input_length=max_text_len))
model.add(LSTM(64, return_sequences=True, dropout=0.2, recurrent_dropout=0.15))
model.add(LSTM(64, return_sequences=False, dropout=0.2, recurrent_dropout=0.15))
model.add(Dense(16))
model.add(Dropout(rate=0.25))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Load pre-trained weights
model.load_weights('model_weights.h5')

# Print the obtained loss and accuracy
print("Loss: {0}\nAccuracy: {1}".format(*model.evaluate(X_test, y_test, verbose=0)))