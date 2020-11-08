# In this exercise, you're going to extract data that resides inside tables of a local PostgreSQL database. The data you'll be using is the Pagila example database. The database backs a fictional DVD store application, and educational resources often use it as an example database. You'll be creating and using a function that extracts a database table into a pandas DataFrame object. The tables you'll be extracting are: film: the films that are rented out in the DVD store. customer: the customers that rented films at the DVD store. In order to connect to the database, you'll have to use a PostgreSQL connection URI, which looks something like this: postgresql://[user[:password]@][host][:port][/database]

# Function to extract table to a pandas DataFrame
def extract_table_to_pandas(tablename, db_engine):
    query = "SELECT * FROM {}".format(tablename)
    return pd.read_sql(query, db_engine)

# Connect to the database using the connection URI
connection_uri = "postgresql://repl:password@localhost:5432/pagila"
db_engine = sqlalchemy.create_engine(connection_uri)

# Extract the film table into a pandas DataFrame
extract_table_to_pandas("film", db_engine)

# Extract the customer table into a pandas DataFrame
extract_table_to_pandas("customer", db_engine)
