# Print the model summary
model_cnn.summary()

# Load pre-trained weights
model_cnn.load_weights('model_weights.h5')

# Evaluate the model to get the loss and accuracy values
loss, acc = model_cnn.evaluate(x_test, y_test, verbose=0)

# Print the loss and accuracy obtained
print("Loss: {0}\nAccuracy: {1}".format(loss, acc))