# Import StandardScaler
from sklearn.preprocessing import StandardScaler

# Initialize StandardScaler
sc = StandardScaler()

# Fit the scaler
sc.fit(environment)

# Print mean and variance
print(sc.mean_)
print(sc.var_)