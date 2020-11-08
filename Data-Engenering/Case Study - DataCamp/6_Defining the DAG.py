# In the previous exercises, you've completed the extract, transform and load phases separately. Now all of this is put together in one neat etl() function that you can discover in the console. The etl() function extracts raw course and ratings data from relevant databases, cleans corrupt data and fills in missing value, computes average rating per course and creates recommendations based on the decision rules for producing recommendations, and finally loads the recommendations into a database. As you might remember from the video, etl() accepts a single argument: db_engines. You can pass this to the task using op_kwargs in the PythonOperator. You can pass it a dictionary that will be filled in as kwargs in the callable.
# Define the DAG so it runs on a daily basis
dag = DAG(dag_id="recommendations",
          schedule_interval='0 0 * * *')

# Make sure `etl()` is called in the operator. Pass the correct kwargs.
task_recommendations = PythonOperator(
    task_id="recommendations_task",
    python_callable=etl,
    op_kwargs={"db_engines": db_engines},
)
# Enable the DAG
# It's time to enable the DAG you just created, so it can start running on a daily schedule. To the right you can find the Airflow interface. The DAG you created is called recommendations.
