# Create a python list of numbers from 1 to 100
numb = range(1, 100)

# Load the list into PySpark
spark_data = sc.parallelize(numb)
