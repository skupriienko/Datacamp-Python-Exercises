# Importing the speech_recognition library
import speech_recognition as sr
import wave

# Create an instance of the Recognizer class
recognizer = sr.Recognizer()

# # Set the energy threshold
# recognizer.energy_threshold = 300
# clean_support_call_audio = open('e:/src/Datacamp/Natural Language Processing in Python/Spoken Language Processing in Python/clean-support-call.wav', 'r')
harvard = sr.AudioFile('e:/src/Datacamp/Natural Language Processing in Python/Spoken Language Processing in Python/clean-support-call.wav')
with harvard as source:
    clean_support_call_audio = recognizer.record(source)

# Transcribe the support call audio
text = recognizer.recognize_google(audio_data=clean_support_call_audio, language='en-US')

print(text)
