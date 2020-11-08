# A great way to recommend courses is to recommend top-rated courses, as DataCamp students often like courses that are highly rated by their peers. In this exercise, you'll complete a transformation function transform_avg_rating() that aggregates the rating data using the pandas DataFrame's .groupby() method. The goal is to get a DataFrame with two columns, a course id and its average rating: course_id	avg_rating 123	4.72 111	4.62 ...	... In this exercise, you'll complete this transformation function, and apply it on raw rating data extracted via the helper function extract_rating_data() which extracts course ratings from the rating table.

# Complete the transformation function
def transform_avg_rating(rating_data):
  # Group by course_id and extract average rating per course
  avg_rating = rating_data.groupby('course_id').rating.mean()
  # Return sorted average ratings per course
  sort_rating = avg_rating.sort_values(ascending=False).reset_index()
  return sort_rating

# Extract the rating data into a DataFrame
rating_data = extract_rating_data(db_engines)

# Use transform_avg_rating on the extracted data and print results
avg_rating_data = transform_avg_rating(rating_data)
print(avg_rating_data)
