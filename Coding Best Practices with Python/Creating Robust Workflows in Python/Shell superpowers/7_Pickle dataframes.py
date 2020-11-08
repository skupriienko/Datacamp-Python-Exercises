pd.DataFrame(
    np.c_[(diabetes.data, diabetes.target)],
    columns="age sex bmi map tc ldl hdl tch ltg glu target".split()
    # Pickle the diabetes dataframe with zip compression
    ).to_pickle("diabetes.pkl.zip")

# Unpickle the diabetes dataframe
df = pd.read_pickle("diabetes.pkl.zip")
df.plot.scatter(x="ltg", y="target", c="age", colormap="viridis")
plt.show()
