import pyspark

sc = SparkContext
spark = SparkSession

# Verify SparkContext
print(sc)

# Print Spark version
print(sc.version)