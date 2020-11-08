def model_subscribe(client, userdata, message):
    data = json.loads(message.payload)
    # Parse to DataFrame
    df = pd.DataFrame.from_records([data], index="timestamp", columns=cols)
    # Predict result
    category = pl.predict(df)
    if category[0] < 1:
        # Call business logic
        close_window(df, category)
    else:
        print("Nice Weather, nothing to do.")  

# Subscribe model_subscribe to MQTT Topic
subscribe.callback(model_subscribe, topic, hostname=MQTT_HOST)