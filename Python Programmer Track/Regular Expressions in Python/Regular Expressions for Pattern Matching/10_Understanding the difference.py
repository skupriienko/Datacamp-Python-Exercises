# Import re
import re

# Write a regex to eliminate tags
string_notags = re.sub(r"<.+?>", " ", string)

# Print out the result
print(string_notags)
