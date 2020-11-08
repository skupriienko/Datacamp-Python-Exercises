import wave
import numpy as np

# Open good morning sound wave and read frames as bytes
good_morning = wave.open('e:/src/Datacamp/Natural Language Processing in Python/Spoken Language Processing in Python/good-morning.wav', 'r')
signal_gm = good_morning.readframes(-1)

# Convert good morning audio bytes to integers
soundwave_gm = np.frombuffer(signal_gm, dtype='int16')

# View the first 10 sound wave values
print(soundwave_gm[:10])