import pandas as pd
from datetime import datetime

# MODIFY the class to turn created_at into a read-only property
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self._created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self._created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)

    @property
    def created_at(self):
        return self._created_at

ldf = LoggedDF({"col1": [1,2], "col2":[3,4]})

# Put into try-except block to catch AtributeError and print a message
try:
    ldf.created_at = '2035-07-13'
except AttributeError:
    print("Could not set attribute")
