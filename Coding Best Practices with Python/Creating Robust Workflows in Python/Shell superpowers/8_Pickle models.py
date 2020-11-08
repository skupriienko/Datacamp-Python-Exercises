# Train and pickle a linear model
joblib.dump(LinearRegression().fit(x_train, y_train), "linear.pkl")

# Unpickle the linear model
linear = joblib.load("linear.pkl")
predictions = linear.predict(x_test)
plt.scatter(y_test, predictions, edgecolors=(0, 0, 0))
min_max = [y_test.min(), y_test.max()]
plt.plot(min_max, min_max, "--", lw=3)
plt.xlabel("Measured")
plt.ylabel("Predicted")
plt.show()
