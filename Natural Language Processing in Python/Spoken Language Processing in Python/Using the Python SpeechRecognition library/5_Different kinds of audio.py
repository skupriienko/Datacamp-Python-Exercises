# Create a recognizer class
recognizer = sr.Recognizer()

# Pass the Japanese audio to recognize_google
text = recognizer.recognize_google(japanese_audio, language='en-US')

# Print the text
print(text)

# Create a recognizer class
recognizer = sr.Recognizer()

# Pass the Japanese audio to recognize_google
text = recognizer.recognize_google(japanese_audio, language='ja')

# Print the text
print(text)

# Create a recognizer class
recognizer = sr.Recognizer()

# Pass the leopard roar audio to recognize_google
text = recognizer.recognize_google(leopard_audio,
                                   language="en-US",
                                   show_all=True)

# Print the text
print(text)

# Create a recognizer class
recognizer = sr.Recognizer()

# Pass charlie_audio to recognize_google
text = recognizer.recognize_google(charlie_audio,
                                   language="en-US")

# Print the text
print(text)
