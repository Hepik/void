import random


class Generator:
    random_list_of_numbers = []

    def __init__(self):
        self.random_list_of_numbers = []
        for i in range(0, 5):
            n = random.randint(1, 100000)
            self.random_list_of_numbers.append(n)


object1 = Generator()
