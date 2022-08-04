import csv

import paho.mqtt.client as mqtt


class Receiver:
    def __init__(self):
        super().__init__()
        self.client2 = mqtt.Client()
        self.client2.connect('localhost')
        self.client2.subscribe('/number/#')
        self.client2.on_message = self.on_message
        self.client2.loop_forever()

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

        with open('numbers.csv', '+') as file:
            writer = csv.writer(file)
            writer.writerow(msg.payload)


receiver = Receiver()

