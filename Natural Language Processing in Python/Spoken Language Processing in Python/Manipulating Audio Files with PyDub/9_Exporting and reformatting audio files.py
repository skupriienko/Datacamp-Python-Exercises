from pydub import AudioSegment

# Import the .mp3 file
mp3_file = AudioSegment.from_file('mp3_file.mp3')

# Export the .mp3 file as wav
mp3_file.export(out_f='mp3_file.wav',
                format='wav')
