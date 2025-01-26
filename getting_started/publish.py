import sys
import paho.mqtt.client as mqtt

topic="/test/topic"
message="Hello from LinuxMantra"
host="localhost"
port=1883

client = mqtt.Client()
CONNACK_ACCEPTED=0

if client.connect(host,port,60) != CONNACK_ACCEPTED:
    print("Error Connecting")
    sys.exit(1)
else:
    print("Connected")

client.publish(topic,message)
client.disconnect()


