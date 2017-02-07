import random
import string


class Robot:
    @staticmethod
    def random_name():
        random.seed()
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(2)) + str(random.randint(0, 999)).zfill(3)

    def __init__(self):
        self.name = Robot.random_name()

    def reset(self):
        self.__init__()
