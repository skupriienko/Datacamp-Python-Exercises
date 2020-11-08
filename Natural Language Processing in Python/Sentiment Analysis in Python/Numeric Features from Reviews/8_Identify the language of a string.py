foreign = 'La histoire rendu étai fidèle, excellent, et grand.'

# Import the language detection function and package
from langdetect import detect_langs

# Detect the language of the foreign string
print(detect_langs(foreign))