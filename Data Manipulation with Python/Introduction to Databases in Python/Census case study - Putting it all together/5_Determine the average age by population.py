# Import select and func
from sqlalchemy import select, func

# Select the average of age weighted by pop2000
stmt = select([func.sum(census.columns.pop2000 * census.columns.age)
  					/ func.sum(census.columns.pop2000)
			  ])
