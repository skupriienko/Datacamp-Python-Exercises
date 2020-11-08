# Import mqtt library
import paho.mqtt.subscribe as subscribe

# Retrieve one message
msg = subscribe.simple("datacamp/iot/simple", hostname="mqtt.datacamp.com")

# Print topic and payload
print(f"{msg.topic}, {msg.payload}")