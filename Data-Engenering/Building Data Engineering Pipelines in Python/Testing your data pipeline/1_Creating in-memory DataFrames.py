from datetime import date
from pyspark.sql import Row

Record = Row("country", "utm_campaign", "airtime_in_minutes", "start_date", "end_date")

# Create a tuple of records
data = (
  Record("USA", "DiapersFirst", 28, date(2017, 1, 20), date(2017, 1, 27)),
  Record("Germany", "WindelKind", 31, date(2017, 1, 25), None),
  Record("India", "CloseToCloth", 32, date(2017, 1, 25), date(2017, 2, 2))
)

# Create a DataFrame from these records
frame = spark.createDataFrame(data)
frame.show()