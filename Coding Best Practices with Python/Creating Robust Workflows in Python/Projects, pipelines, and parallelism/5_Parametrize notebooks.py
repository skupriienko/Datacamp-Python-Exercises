# Read in the notebook to find the default parameter names
pprint(nbformat.read("sklearn.ipynb", as_version=4).cells[0].source)
keys = ["dataset_name", "model_type", "model_name", "hyperparameters"]
vals = ["diabetes", "ensemble", "RandomForestRegressor",
        dict(max_depth=3, n_estimators=100, random_state=0)]
parameter_dictionary = dict(zip(keys, vals))

# Execute the notebook with custom parameters
pprint(pm.execute_notebook(
    "sklearn.ipynb", "rf_diabetes.ipynb",
    kernel_name="python3", parameters=parameter_dictionary
	))
