import wave

# Create audio file wave object
good_morning = wave.open('e:/src/Datacamp/Natural Language Processing in Python/Spoken Language Processing in Python/good-morning.wav', 'r')

# Read all frames from wave object
signal_gm = good_morning.readframes(-1)

# View first 10
print(signal_gm[:10])
