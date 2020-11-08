# Import the embedding layer
from keras.layers import Embedding

# Create a model with embeddings
model = Sequential(name="emb_model")
model.add(Embedding(input_dim=vocabulary_size+1, output_dim=wordvec_dim, input_length=sentence_len, trainable=True))
model.add(GRU(128))
model.add(Dense(1))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Print the summaries of the one-hot model
model_onehot.summary()

# Print the summaries of the model with embeddings
model.summary()