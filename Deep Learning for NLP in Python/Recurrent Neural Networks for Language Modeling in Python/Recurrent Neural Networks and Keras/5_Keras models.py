# Instantiate the class
model = Sequential(name="sequential_model")

# One LSTM layer (defining the input shape because it is the
# initial layer)
model.add(LSTM(128, input_shape=(None, 10), name="LSTM"))

# Add a dense layer with one unit
model.add(Dense(1, activation="sigmoid", name="output"))

# The summary shows the layers and the number of parameters
# that will be trained
model.summary()

# Define the input layer
main_input = Input(shape=(None, 10), name="input")

# One LSTM layer (input shape is already defined)
lstm_layer = LSTM(128, name="LSTM")(main_input)

# Add a dense layer with one unit
main_output = Dense(1, activation="sigmoid", name="output")(lstm_layer)

# Instantiate the class at the end
model = Model(inputs=main_input, outputs=main_output, name="modelclass_model")

# Same amount of parameters to train as before (71,297)
model.summary()

