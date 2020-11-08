# Merging data allows you to combine disparate 
# datasets into a single dataset to do more complex analysis.

# Here, you'll be using survey data that contains readings 
# hat William Dyer, Frank Pabodie, and Valentina Roerich 
# took in the late 1920s and 1930s while they were on 
# an expedition towards Antarctica. The dataset was taken 
# from a sqlite database from the Software Carpentry SQL lesson.
# http://swcarpentry.github.io/sql-novice-survey/

# Merge the DataFrames: o2o
o2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print o2o
print(o2o)
