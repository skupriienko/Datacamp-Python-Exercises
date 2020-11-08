# Import Table, Column, String, and Integer
from sqlalchemy import Table, Column, String, Integer

# Build a census table: census
census = Table('census', metadata,
               Column('state', String(30)),
               Column('sex', String(1)),
               Column('age', Integer),
               Column('pop2000', Integer),
               Column('pop2008', Integer))

# Create the table in the database
metadata.create_all(engine)
