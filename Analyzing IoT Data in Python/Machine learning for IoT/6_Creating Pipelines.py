# Import pipeline
from sklearn.pipeline import Pipeline

# Create Scaler and Regression objects
sc = StandardScaler()
logreg = LogisticRegression()

# Create Pipeline
pl = Pipeline([
        ("scale", sc),
        ("logreg", logreg)
    ])

# Fit the pipeline and print predictions
pl.fit(X_train, y_train)
print(pl.predict(X_test))