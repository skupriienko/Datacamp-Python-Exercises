# Plot the images on a subplots array 
fig, axes = plt.subplots(1, 4)

# Loop through subplots and draw image
for ii in range(4):
    im = vol[ii*40, :, :]
    axes[ii].imshow(im, cmap='gray')
    axes[ii].axis('off')
    
# Render the figure
plt.show()