import random
from time import sleep


class Generator:

    def get_random_numbers(self):
        while True:
            number = random.randint(1, 100000)
            yield number
            sleep(1)


generator = Generator()
