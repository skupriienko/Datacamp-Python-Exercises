# Combine the dataframes
environ_traffic = pd.concat([environ, traffic], axis=1)

# Print first 5 rows
print(environ_traffic.head())

# Create agg logic
agg_dict = {"temperature": "max", "humidity": "max", "sunshine": "sum", 
            "light_veh": "sum", "heavy_veh": "sum",
            }

# Resample the dataframe 
environ_traffic_resampled = environ_traffic.resample('1h').agg(agg_dict)
print(environ_traffic_resampled.head())