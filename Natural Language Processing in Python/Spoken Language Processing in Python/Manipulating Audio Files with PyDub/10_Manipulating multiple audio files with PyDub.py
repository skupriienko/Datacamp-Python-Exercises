# Loop through the files in the folder
for audio_file in folder:

	# Create the new .wav filename
    wav_filename = os.path.splitext(os.path.basename(audio_file))[0] + ".wav"

    # Read audio_file and export it in wav format
    AudioSegment.from_file(audio_file).export(out_f=wav_filename,
                                      format='wav')

    print(f"Creating {wav_filename}...")
