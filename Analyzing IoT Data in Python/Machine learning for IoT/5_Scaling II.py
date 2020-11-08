# Initialize StandardScaler
sc = StandardScaler()

# Fit the scaler
sc.fit(environment)

# Transform the data
environ_scaled = sc.transform(environment)

# Convert scaled data to DataFrame
environ_scaled = pd.DataFrame(environ_scaled, 
                              columns=environment.columns, 
                              index=environment.index)
print(environ_scaled.head())
plot_unscaled_scaled(environment, environ_scaled)