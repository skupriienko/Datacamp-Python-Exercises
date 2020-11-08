import imageio
import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

im = imageio.imread("C:/src/SANDBOX/LEARNING/Datacamp/Image Processing in Python/Biomedical Image Analysis in Python/hand.png") 
 
# Smooth intensity values
im_filt = ndi.median_filter(im, size=3) 

# Select high-intensity pixels
mask_start = np.where(im_filt > 60, 1, 0)
mask = ndi.binary_closing(mask_start)

# Label the objects in "mask"
labels, nlabels = ndi.label(mask)
print('Num. Labels:', nlabels)

# Create a `labels` overlay
overlay = np.where(labels > 0, labels, np.nan)

# Use imshow to plot the overlay
# plt.imshow(overlay, cmap='rainbow', alpha=0.75) 
# plt.show()

# Select objects
# Label the image "mask"
labels, nlabels = ndi.label(mask)

# Select left ventricle pixels
lv_val = labels[128, 128]
lv_mask = np.where(labels == lv_val, 1, np.nan)

# Overlay selected label
plt.imshow(lv_mask, cmap='rainbow')
plt.show() 

# Extract objects

# Create left ventricle mask
labels, nlabels = ndi.label(mask)
lv_val = labels[128, 128]
lv_mask = np.where(labels == lv_val, 1, 0)

# Find bounding box of left ventricle
bboxes = ndi.find_objects(lv_mask)
print('Number of objects:', len(bboxes))
print('Indices for first box:', bboxes[0])

# Crop to the left ventricle (index 0)
im_lv = im[bboxes[0]]

# Plot the cropped image
plt.imshow(im_lv) 
plt.show() 