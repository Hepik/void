import random


class Generator:

    def get_random_numbers(self):
        while True:
            number = random.randint(1, 100000)
            yield number


object1 = Generator()
