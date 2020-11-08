# Create LogisticRegression model
logreg = LogisticRegression()

# Fit the model
logreg.fit(X_train, y_train)

# Score the model
print(logreg.score(X_train, y_train))
print(logreg.score(X_test, y_test))