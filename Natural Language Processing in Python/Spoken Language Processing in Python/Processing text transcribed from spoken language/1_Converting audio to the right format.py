# Create function to convert audio file to wav
def convert_to_wav(filename):
  """Takes an audio file of non .wav format and converts to .wav"""
  # Import audio file
  audio = AudioSegment.from_file(filename)

  # Create new filename
  new_filename = filename.split(".")[0] + ".wav"

  # Export file as .wav
  audio.export(new_filename, format='wav')
  print(f"Converting {filename} to {new_filename}...")

# Test the function
convert_to_wav('call_1.mp3')
