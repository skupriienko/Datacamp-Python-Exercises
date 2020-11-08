def transcribe_audio(filename):
    """Takes a .wav format audio file and transcribes it to text."""
    # Setup a recognizer instance
    recognizer = sr.Recognizer()

    # Import the audio file and convert to audio data
    audio_file = sr.AudioFile(filename)
    with audio_file as source:
        audio_data = recognizer.record(source)

    # Return the transcribed text
    return recognizer.recognize_google(audio_data)

# Test the function
print(transcribe_audio("call_1.wav"))
