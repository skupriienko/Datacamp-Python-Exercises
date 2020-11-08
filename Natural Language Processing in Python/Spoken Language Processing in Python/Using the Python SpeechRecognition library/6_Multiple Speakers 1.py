# Create a recognizer class
recognizer = sr.Recognizer()

# Recognize the multiple speaker AudioData
text = recognizer.recognize_google(multiple_speakers,
                       			   language='en-US')

# Print the text
print(text)
