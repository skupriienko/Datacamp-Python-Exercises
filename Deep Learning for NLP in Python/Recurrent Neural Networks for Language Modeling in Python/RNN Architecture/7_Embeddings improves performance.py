# Create the model with embedding
model = Sequential(name="emb_model")
model.add(Embedding(input_dim=max_vocabulary, output_dim=wordvec_dim, input_length=max_len))
model.add(SimpleRNN(units=128))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Load pre-trained weights
model.load_weights('embedding_model_weights.h5')

# Evaluate the models' performance (ignore the loss value)
_, acc_embeddings = model.evaluate(X_test, y_test, verbose=0)

# Print the results
print("SimpleRNN model's accuracy:\t{0}\nEmbeddings model's accuracy:\t{1}".format(acc_simpleRNN, acc_embeddings))