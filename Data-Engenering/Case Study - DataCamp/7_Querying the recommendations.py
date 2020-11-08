# In the previous exercises, you've learned how to calculate a table with course recommendations on a daily basis. Now that this recommendations table is in the data warehouse, you could also quickly join it with other tables in order to produce important features for DataCamp students such as customized marketing emails, intelligent recommendations for students and other features. In this exercise, you will get a taste of how the newly created recommendations table could be utilized by creating a function recommendations_for_user() which automatically gets the top recommended courses based per user ID for a particular rating threshold.

def recommendations_for_user(user_id, threshold=4.5):
    # Join with the courses table
    query = """
    SELECT title, rating FROM recommendations
        INNER JOIN courses ON courses.course_id = recommendations.course_id
        WHERE user_id=%(user_id)s AND rating>%(threshold)s
        ORDER BY rating DESC
    """
    # Add the threshold parameter
    predictions_df = pd.read_sql(query, db_engine, params = {"user_id": user_id,
                                                           "threshold": threshold})
    return predictions_df.title.values

# Try the function you created
print(recommendations_for_user(12, 4.65))
