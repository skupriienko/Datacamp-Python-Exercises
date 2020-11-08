# Convert mp3 file to wav
convert_to_wav("call_1.mp3")

# Check the stats of new file
call_1 = show_pydub_stats("call_1.wav")

# Split call_1 to mono
call_1_split = call_1.split_to_mono()

# Export channel 2 (the customer channel)
call_1_split[1].export("call_1_channel_2.wav",
                       format="wav")

# Transcribe the single channel
print(transcribe_audio("call_1_channel_2.wav"))
