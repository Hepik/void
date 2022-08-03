import random


class Generator:

    def __init__(self):
        self.random_list_of_numbers = self.get_random_numbers()

    def get_random_numbers(self):
        random_list_of_numbers = []
        for i in range(0, 5):
            n = random.randint(1, 100000)
            random_list_of_numbers.append(n)
        return random_list_of_numbers


object1 = Generator()
print(object1.random_list_of_numbers[1])