from datetime import datetime
import paho.mqtt.client as mqtt


class Receiver:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.connect('localhost')
        self.client.subscribe('/number/#')
        self.client.on_message = self._on_message
        self.client.loop_forever()

    def _on_message(self, client, userdata, msg):
        print(f'{msg.topic} {msg.payload}')
        dt = datetime.now()
        ts = datetime.timestamp(dt)

        with open('numbers.csv', 'a') as file:
            file.write(f"{ts}\t{msg.payload.decode()}\n")


if __name__ == '__main__':
    Receiver()
