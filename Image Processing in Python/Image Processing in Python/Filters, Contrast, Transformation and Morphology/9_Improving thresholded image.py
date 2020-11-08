# Import the module
from skimage import morphology

# Obtain the dilated image
dilated_image = morphology.dilation(world_image)

# See results
show_image(world_image, 'Original')
show_image(dilated_image, 'Dilated image')
