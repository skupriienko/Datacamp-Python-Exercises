def show_pydub_stats(filename):
    """Returns different audio attributes related to an audio file."""
    # Create AudioSegment instance
    audio_segment = AudioSegment.from_file(filename)

    # Print audio attributes and return AudioSegment instance
    print(f"Channels: {audio_segment.channels}")
    print(f"Sample width: {audio_segment.sample_width}")
    print(f"Frame rate (sample rate): {audio_segment.frame_rate}")
    print(f"Frame width: {audio_segment.frame_width}")
    print(f"Length (ms): {len(audio_segment)}")
    return audio_segment

# Try the function
call_1_audio_segment = show_pydub_stats("call_1.wav")
