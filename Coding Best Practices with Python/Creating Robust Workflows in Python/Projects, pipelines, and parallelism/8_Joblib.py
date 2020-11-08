# Set up a Dask client with 4 threads and 1 worker
Client(processes=False, threads_per_worker=4, n_workers=1)

# Run grid search using joblib and a Dask backend
with joblib.parallel_backend("dask"):
    engrid.fit(x_train, y_train)

plot_enet(*enet_path(x_test, y_test, eps=5e-5, fit_intercept=False,
                    l1_ratio=engrid.best_params_["l1_ratio"])[:2])
