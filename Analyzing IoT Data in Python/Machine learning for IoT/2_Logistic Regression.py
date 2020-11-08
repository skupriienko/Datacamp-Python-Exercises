# Import LogisticRegression
from sklearn.linear_model import LogisticRegression

# Initialize the model
logreg = LogisticRegression()

# Fit the model
logreg.fit(X_train, y_train)

# Predict classes
print(logreg.predict(X_test))