import paho.mqtt.client as mqtt

from generator import Generator


class Sender:
    def __init__(self, generator: Generator):
        print("<<<START>>>")
        self.generator = generator
        self.client = mqtt.Client()
        self.client.connect('localhost')

    def post(self, number):
        print("posting...")

        number = str(number)

        self.client.publish('/number', payload=number, qos=0, retain=False)

    def get_numbers(self):
        for i in self.generator.get_random_numbers():
            self.post(i)

    def _on_message(self, client, userdata, msg):
        print(f'{msg.topic} {msg.payload}')


if __name__ == '__main__':
    gen = Generator(1, 1000000, 1)
    sender = Sender(gen)
    sender.get_numbers()
