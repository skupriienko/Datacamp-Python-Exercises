# from pyspark import SparkContext
# sc = SparkContext(appName = "test")


# file_path = 'E:\src\SANDBOX\LEARNING\Datacamp\Data-Engenering\Big Data Fundamentals with PySpark\5000_points.txt'

# Load the dataset into a RDD
clusterRDD = sc.textFile(file_path)

# Split the RDD based on tab
rdd_split = clusterRDD.map(lambda x: x.split('\t'))

# Transform the split RDD by creating a list of integers
rdd_split_int = rdd_split.map(lambda x: [int(x[0]), int(x[1])])

# Count the number of rows in RDD
print("There are {} rows in the rdd_split_int dataset".format(rdd_split_int.count()))
