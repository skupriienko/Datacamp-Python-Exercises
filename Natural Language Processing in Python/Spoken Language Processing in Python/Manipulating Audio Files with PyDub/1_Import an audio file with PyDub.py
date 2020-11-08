# Import AudioSegment from Pydub
from pydub import AudioSegment

# Create an AudioSegment instance
wav_file = AudioSegment.from_file(file='wav_file.wav',
                                  format="wav")

# Check the type
print(type(wav_file))
