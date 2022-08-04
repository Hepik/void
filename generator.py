import random
from time import sleep


class Generator:
    def __init__(self, sleep_time: int, max_value: int, min_value: int):
        self.sleep_time = sleep_time
        self.max_value = max_value
        self.min_value = min_value

    def get_random_numbers(self):
        while True:
            number = random.randint(self.min_value, self.max_value)
            yield number
            sleep(self.sleep_time)
