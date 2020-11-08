# Import ImageIO and load image
import imageio
im = imageio.imread("chest-220.dcm")

# Print the available metadata fields
print(im.meta.keys())