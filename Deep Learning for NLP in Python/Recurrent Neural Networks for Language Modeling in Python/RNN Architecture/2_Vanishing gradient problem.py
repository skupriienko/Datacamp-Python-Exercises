# Create the model
model = Sequential()
model.add(SimpleRNN(units=600, input_shape=(None, 1)))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Load pre-trained weights
model.load_weights('model_weights.h5')

# Plot the accuracy x epoch graph
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.legend(['train', 'val'], loc='upper left')
plt.show()