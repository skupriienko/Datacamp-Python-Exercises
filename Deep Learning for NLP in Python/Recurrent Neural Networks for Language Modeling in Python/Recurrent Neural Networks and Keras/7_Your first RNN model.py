# Build model
model = Sequential()
model.add(SimpleRNN(units=128, input_shape=(None, 1)))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Load pre-trained weights
model.load_weights('model_weights.h5')

# Method '.evaluate()' shows the loss and accuracy
loss, acc = model.evaluate(x_test, y_test, verbose=0)
print("Loss: {0} \nAccuracy: {1}".format(loss, acc))
