import paho.mqtt.client as mqtt

from generator import Generator, generator


class Sender(Generator):
    def __init__(self):
        print("<<<START>>>")
        super().__init__()
        self.client = mqtt.Client()
        self.client.connect('localhost')
        self.client.on_connect = self._on_connect
        self.client.loop_forever()

    def post(self, number):
        print("posting...")

        number = str(number)

        self.client.publish('/number', payload=number, qos=0, retain=False)

    def _on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.poster()


    def poster(self):
        for i in generator.get_random_numbers():
            self.post(i)

    def _on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        print(f'{msg.topic} {msg.payload}')


sender = Sender()
