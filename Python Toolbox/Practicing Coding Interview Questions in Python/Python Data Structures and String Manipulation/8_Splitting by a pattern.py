import re

movies = ['1984, 1984, Michael Radford',
 'The Good, the Bad and the Ugly, 1966, Sergio Leone',
 'Terminator 2: Judgment Day, 1991, James Cameron',
 "Harry Potter and the Philosopher's Stone, 2001, Chris Columbus",
 'Back to the Future, 1985, Robert Zemeckis',
 'No Country for Old Men, 2007, Joel Coen, Ethan Coen']

# Compile a regular expression
pattern = re.compile(r', \d+, ')

movies_without_year = []
for movie in movies:
    # Retrieve a movie name and its director
    split_result = re.split(pattern, movie)
    # Create a new string with a movie name and its director
    movie_and_director = ', '.join(split_result)
    # Append the resulting string to movies_without_year
    movies_without_year.append(movie_and_director)

for movie in movies_without_year:
    print(movie)
