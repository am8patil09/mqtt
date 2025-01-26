import sys
import paho.mqtt.client as mqtt

topic="/test/topic"
host="localhost"
port=1883

client = mqtt.Client()
CONNACK_ACCEPTED=0

def handle_testtopic(client, userdata, msg):
    print(f"Message Recieved: {msg.topic} {msg.payload}")


if client.connect(host,port,60) != CONNACK_ACCEPTED:
    print("Error Connecting")
    sys.exit(1)
else:
    print("Connected")

client.on_message = handle_testtopic

client.subscribe(topic)

try:
    client.loop_forever()
except:
    print("Exception")
finally:
    client.disconnect()


