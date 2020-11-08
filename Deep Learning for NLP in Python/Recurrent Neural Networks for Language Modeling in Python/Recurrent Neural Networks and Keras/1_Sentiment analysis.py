# Inspect the first sentence on `X_test`
print(X_test[0])

# Get the predicion for all the sentences
pred = model.predict(X_test)

# Transform the predition into positive (> 0.5) or negative (<= 0.5)
pred_sentiment = ["positive" if x>0.5 else "negative" for x in pred]

# Create a data frame with sentences, predictions and true values
result = pd.DataFrame({'sentence': sentences, 'y_pred': pred_sentiment, 'y_true': y_test})

# Print the first lines of the data frame
print(result.head())

