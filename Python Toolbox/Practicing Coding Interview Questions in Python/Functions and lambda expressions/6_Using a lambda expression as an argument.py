words = ['car',
 'truck',
 'interview',
 'tequila',
 'time',
 'cell',
 'chicken',
 'leader',
 'government',
 'transaction',
 'country',
 'bag',
 'call',
 'area',
 'service',
 'phone',
 'advantage',
 'job',
 'shape',
 'item',
 'atmosphere',
 'height',
 'creature',
 'plane',
 'unit']

# Sort words by the string length
words.sort(key=lambda s: len(s))
print(words)

# Sort words by the last character in a string
words.sort(key=lambda z: z[-1])
print(words)

# Sort words by the total amount of certain characters
words.sort(key=lambda s: s.count('a') + s.count('b') + s.count('c'))
print(words)