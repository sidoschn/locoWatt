import paho.mqtt.client as mqtt
import json

class mqttInterface:
    mqttc = None
    defaultServerIp = "127.0.0.1"
    defaultPort = 1883
    defaultBaseChannel = "locowatt"
    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("locowatt/testInput")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    def startListening(self):
        self.mqttc.loop_forever()

    def publishPayload(self, payload, publishChannel):
        self.mqttc.publish(self.baseChannel+"/"+publishChannel, json.dumps(payload))

    def __init__(self, serverIp = defaultServerIp, port = defaultPort, baseChannel = defaultBaseChannel):

        self.mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_message = self.on_message
        self.baseChannel = baseChannel
        self.mqttc.connect(serverIp, port, 60)
        
        # publishChannel = "testChannel"
        # payload = "MT"
        # self.mqttc.publish("locowatt/"+publishChannel, payload)

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        