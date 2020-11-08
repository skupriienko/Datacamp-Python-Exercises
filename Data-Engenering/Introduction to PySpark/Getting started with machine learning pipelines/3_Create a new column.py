# Create the column plane_age
model_data = model_data.withColumn("plane_age", (model_data.year - model_data.plane_year))