import paho.mqtt.client as mqtt

from generator import Generator, object1


class Sender(Generator):
    def __init__(self):
        print("<<<START>>>")
        super().__init__()
        self.client = mqtt.Client()
        self.client.connect('localhost')
        self.client.on_connect = self._on_connect
        self.client.loop_forever()

    def post(self):
        print("posting...")
        numbers = str(object1.random_list_of_numbers)

        self.client.publish('/numbers', payload=numbers, qos=0, retain=False)

    def _on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.post()

    def _on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))


sender = Sender()
