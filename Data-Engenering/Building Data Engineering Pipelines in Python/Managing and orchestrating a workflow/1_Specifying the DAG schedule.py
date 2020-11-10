from datetime import datetime
from airflow import DAG

reporting_dag = DAG(
    dag_id="publish_EMEA_sales_report", 
    # Insert the cron expression
    schedule_interval="0 7 * * 1",
    start_date=datetime(2019, 11, 24),
    default_args={"owner": "sales"}
)