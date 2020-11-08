#  In the previous exercises you applied the three steps in the ETL process: Extract: Extract the film PostgreSQL table into pandas. Transform: Split the rental_rate column of the film DataFrame. Load: Load a the film DataFrame into a PostgreSQL data warehouse. The functions extract_film_to_pandas(), transform_rental_rate() and load_dataframe_to_film() are defined in your workspace. In this exercise, you'll add an ETL task to an existing DAG. The DAG to extend and the task to wait for are defined in your workspace are defined as dag and wait_for_table respectively.
# Define the ETL function
def etl():
    film_df = extract_film_to_pandas()
    film_df = transform_rental_rate(film_df)
    load_dataframe_to_film(film_df)

# Define the ETL task using PythonOperator
etl_task = PythonOperator(task_id='etl_film',
                          python_callable=etl,
                          dag=dag)

# Set the upstream to wait_for_table and sample run etl()
etl_task.set_upstream(wait_for_table)
etl()
