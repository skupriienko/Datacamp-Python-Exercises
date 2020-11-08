# Create Pipeline
pl = Pipeline([
        ('scale', StandardScaler()),
  		('logreg', LogisticRegression())
    ])

# Fit the pipeline
pl.fit(X_train, y_train)

# Predict classes
predictions = pl.predict(X_test)

# Print results
print(predictions)