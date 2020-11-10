# Create a DAG object
dag = DAG(
  dag_id='optimize_diaper_purchases',
  default_args={
    # Don't email on failure
    'email_on_failure': False,
    # Specify when tasks should have started earliest
    'start_date': datetime(2019, 6, 25)
  },
  # Run the DAG daily
  schedule_interval='@daily')