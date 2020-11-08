cache = []

def on_message(client, userdata, message):
 	# Combine timestamp and payload
    data = f"{message.timestamp},{message.payload}"
    # Append data to cache
    cache.append(data)
    # Check cache length
    if len(cache) > MAX_CACHE:
        with Path("energy.txt").open("a") as f:
            # Save to file
            f.writelines(cache)
        # reset cache
        cache.clear()

# Connect function to mqtt datastream
subscribe.callback(on_message, topics="datacamp/energy", hostname=MQTT_HOST)