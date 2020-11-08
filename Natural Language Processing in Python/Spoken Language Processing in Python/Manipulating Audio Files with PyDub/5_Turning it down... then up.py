from pydub import AudioSegment

# Import audio file
volume_adjusted = AudioSegment.from_file('volume_adjusted.wav')

# Lower the volume by 60 dB
quiet_volume_adjusted = volume_adjusted - 60

from pydub import AudioSegment

# Import audio file
volume_adjusted = AudioSegment.from_file('volume_adjusted.wav')

# Increase the volume by 15 dB
louder_volume_adjusted = volume_adjusted + 15
