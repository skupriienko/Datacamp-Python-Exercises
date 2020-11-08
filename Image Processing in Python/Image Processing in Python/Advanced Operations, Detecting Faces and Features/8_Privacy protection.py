# Detect the faces
detected = detector.detect_multi_scale(img=group_image,
                                       scale_factor=1.2, step_ratio=1,
                                       min_size=(10, 10), max_size=(100, 100))
# For each detected face
for d in detected:
    # Obtain the face rectangle from detected coordinates
    face = getFaceRectangle(d)

    # Apply gaussian filter to extracted face
    blurred_face = gaussian(face, multichannel=True, sigma = 8)

    # Merge this blurry face to our final image and show it
    resulting_image = mergeBlurryFace(group_image, blurred_face)
show_image(resulting_image, "Blurred faces")
