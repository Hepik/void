# import csv

import paho.mqtt.client as mqtt


class Receiver:
    def __init__(self):
        super().__init__()
        self.client2 = mqtt.Client()
        self.client2.connect('localhost')
        self.client2.subscribe('/number/#')
        self.client2.on_message = self._on_message
        self.client2.loop_forever()

    def _on_message(self, client, userdata, msg):
        print(f'{msg.topic} {msg.payload}')

        with open('numbers.csv', 'a') as file:
            file.write(msg.payload.decode() + '\n')

            # writer = csv.writer(file)'
            # writer.writerow(msg.payload)


if __name__ == '__main__':
    Receiver()
