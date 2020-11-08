# Complete the connection URI
connection_uri = "postgresql://repl:password@localhost:5432/datacamp_application"
db_engine = sqlalchemy.create_engine(connection_uri)

# Get user with id 4387
user1 = pd.read_sql("SELECT * FROM rating where user_id = '4387'", db_engine)

# Get user with id 18163
user2 = pd.read_sql("SELECT * FROM rating where user_id = '18163'", db_engine)

# Get user with id 8770
user3 = pd.read_sql("SELECT * FROM rating where user_id = '8770'", db_engine)

# Use the helper function to compare the 3 users
print_user_comparison(user1, user2, user3)
