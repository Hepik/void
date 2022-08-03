import paho.mqtt.client as mqtt


class Receiver:
    def __init__(self):
        super().__init__()
        self.client2 = mqtt.Client()
        self.client2.connect('localhost')
        self.client2.subscribe('/numbers/#')
        self.client2.on_message = self.on_message
        self.client2.loop_forever()

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

        with open('Numbers', 'wb') as file:
            file.write(msg.payload)


receiver = Receiver()

