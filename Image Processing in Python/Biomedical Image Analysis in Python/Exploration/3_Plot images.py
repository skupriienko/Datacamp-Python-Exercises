# Import ImageIO and PyPlot 
import imageio
import matplotlib.pyplot as plt

# Read in "chest-220.dcm"
im = imageio.imread("chest-220.dcm")


# Draw the image in grayscale
plt.imshow(im, cmap='gray')

# Render the image
plt.show()


# Draw the image with greater contrast
plt.imshow(im, vmin=-200, vmax=200, cmap='gray')

# Render the image
plt.show()

# Remove axis ticks and labels
plt.axis('off')

# Render the image
plt.show()