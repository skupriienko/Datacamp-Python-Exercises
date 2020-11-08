# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Find the frame rate
print(wav_file.frame_rate)


# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Find the number of channels
print(wav_file.channels)

# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Find the max amplitude
print(wav_file.max)

# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Find the length
print(len(wav_file))
