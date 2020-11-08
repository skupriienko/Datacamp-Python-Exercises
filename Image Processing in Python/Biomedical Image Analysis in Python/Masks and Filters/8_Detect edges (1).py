# Set weights to detect vertical edges
weights = [[1,0,-1], [1,0,-1], [1,0,-1]]

# Convolve "im" with filter weights
edges = ndi.convolve(im, weights)

# Draw the image in color
plt.imshow(edges, vmin=-150, vmax=150, cmap='seismic')
plt.colorbar()
format_and_render_plot()