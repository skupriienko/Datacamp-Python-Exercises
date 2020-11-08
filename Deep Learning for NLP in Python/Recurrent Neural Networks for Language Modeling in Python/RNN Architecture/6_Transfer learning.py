# Load the glove pre-trained vectors
glove_matrix = load_glove('glove_200d.zip')

# Create a model with embeddings
model = Sequential(name="emb_model")
model.add(Embedding(input_dim=vocabulary_size + 1, output_dim=wordvec_dim,
                    embeddings_initializer=Constant(glove_matrix),
                    input_length=sentence_len, trainable=False))
model.add(GRU(128))
model.add(Dense(1))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Print the summaries of the model with embeddings
model.summary()