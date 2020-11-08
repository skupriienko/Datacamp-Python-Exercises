# Import sqlite3
import sqlite3

# Open connection to DB
conn = sqlite3.connect('E:/src/Datacamp/Natural Language Processing in Python/Building Chatbots in Python/hotels.db')

# Create a cursor
c = conn.cursor()

# Define area and price
area, price = "south", "hi"
t = (area, price)

# Execute the query
c.execute('SELECT * FROM hotels WHERE area=? AND price=?', t)

# Print the results
print(c.fetchall())