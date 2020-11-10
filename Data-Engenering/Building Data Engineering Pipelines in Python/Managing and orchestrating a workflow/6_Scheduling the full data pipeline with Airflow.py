spark_args = {"py_files": dependency_path,
              "conn_id": "spark_default"}
# Define ingest, clean and transform job.
with dag:
    ingest = BashOperator(task_id='Ingest_data', bash_command='tap-marketing-api | target-csv --config %s' % config)
    clean = SparkSubmitOperator(application=clean_path, task_id='clean_data', **spark_args)
    insight = SparkSubmitOperator(application=transform_path, task_id='show_report', **spark_args)
    
    # set triggering sequence
    ingest >> clean >> insight