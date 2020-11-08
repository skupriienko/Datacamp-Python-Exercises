# Import pandas as pd
import pandas as pd
from datetime import datetime
# Define LoggedDF inherited from pd.DataFame and add the constructor


class LoggedDF(pd.DataFrame):

    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self.created_at = datetime.today()


ldf = LoggedDF({"col1": [1, 2], "col2": [3, 4]})
print(ldf.values)
print(ldf.created_at)


# Import pandas as pd

# Define LoggedDF inherited from pd.DataFame and add the constructor

class LoggedDF(pd.DataFrame):

    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self.created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        # Copy self to a temporary DataFrame
        temp = self.copy()

        # Create a new column filled with self.created at
        temp["created_at"] = self.created_at

        # Call pd.DataFrame.to_csv on temp with *args and **kwargs
        pd.DataFrame.to_csv(temp, *args, **kwargs)
