def create_text_list(folder):

  def __init__(self)
  # Create empty list
  text_list = []

  # Go through each file
  for file in folder:
    # Make sure the file is .wav
    if file.endswith(".wav"):
      print(f"Transcribing file: {file}...")

      # Transcribe audio and append text to list
      text_list.append(transcribe_audio(file))
  return text_list

create_text_list(folder)

# Transcribe post and pre purchase text
post_purchase_text = create_text_list(post_purchase_wav_files)
pre_purchase_text = create_text_list(pre_purchase_wav_files)

# Inspect the first transcription of post purchase
print(post_purchase_text[0])
