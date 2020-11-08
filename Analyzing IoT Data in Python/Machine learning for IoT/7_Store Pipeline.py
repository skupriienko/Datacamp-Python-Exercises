 # Create Pipeline
pl = Pipeline([
        ("scale", StandardScaler()),
        ("logreg", LogisticRegression())
    ])

# Fit the pipeline
pl.fit(X_train, y_train)

# Store the model
with Path("pipeline.pkl").open('bw') as f:
	pickle.dump(pl, f)
  
# Load the pipeline
with Path("pipeline.pkl").open('br') as f:
	pl_loaded = pickle.load(f)

print(pl_loaded)