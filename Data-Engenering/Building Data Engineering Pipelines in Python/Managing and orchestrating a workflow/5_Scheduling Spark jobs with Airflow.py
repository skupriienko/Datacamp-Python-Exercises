# Import the operator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

# Set the path for our files.
entry_point = os.path.join(os.environ["AIRFLOW_HOME"], "scripts", "clean_ratings.py")
dependency_path = os.path.join(os.environ["AIRFLOW_HOME"], "dependencies", "pydiaper.zip")

with DAG('data_pipeline', start_date=datetime(2019, 6, 25),
         schedule_interval='@daily') as dag:
  	# Define task clean, running a cleaning job.
    clean_data = SparkSubmitOperator(
        application=entry_point, 
        py_files=dependency_path,
        task_id='clean_data',
        conn_id='spark_default')