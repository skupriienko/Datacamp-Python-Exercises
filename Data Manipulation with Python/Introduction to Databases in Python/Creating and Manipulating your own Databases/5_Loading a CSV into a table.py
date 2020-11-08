# import pandas
import pandas as pd

# read census.csv into a dataframe : census_df
census_df = pd.read_csv("census.csv", header=None)

# rename the columns of the census dataframe
census_df.columns = ['state', 'sex', 'age', 'pop2000', 'pop2008']

# append the data from census_df to the "census" table via connection
census_df.to_sql(name='census', con=connection, if_exists='append', index=False)
