from tweepy import Stream

# Set up words to track
keywords_to_track = ['#rstats', '#python']

# Instantiate the SListener object 
listen = SListener(api)

# Instantiate the Stream object
stream = Stream(auth, listen)

# Begin collecting data
stream.filter(track = keywords_to_track)