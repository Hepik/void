import random
from abc import ABC
from time import sleep


class Generator(ABC):
    def __init__(self, sleep_time: int = 1, max_value: int = 1000000, min_value: int = 1):
        self.sleep_time = sleep_time
        self.max_value = max_value
        self.min_value = min_value

    def get_random_numbers(self):
        while True:
            number = random.randint(self.min_value, self.max_value)
            yield number
            sleep(self.sleep_time)
