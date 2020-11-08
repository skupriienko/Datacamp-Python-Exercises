# Import the morphology module
from skimage import morphology

# Obtain the eroded shape
eroded_image_shape = morphology.binary_erosion(upper_r_image)

# See results
show_image(upper_r_image, 'Original')
show_image(eroded_image_shape, 'Eroded image')
