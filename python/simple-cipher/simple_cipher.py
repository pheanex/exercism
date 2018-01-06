import random
import string


def shift(message, key="a", shift_right=True):
    message = [letter.lower() for letter in message if letter.isalpha()]
    for index, letter in enumerate(message):
        delta = ord(key[index % len(key)]) - 97
        if not shift_right:
            delta *= -1
        letter_shifted = chr(97 + (ord(letter) - 97 + delta) % 26)
        message[index] = letter_shifted
    return ''.join(message)


class Caesar:
    @staticmethod
    def encode(message):
        return shift(message, "d", True)

    @staticmethod
    def decode(message):
        return shift(message, "d", False)


class Cipher:
    def __init__(self, key=''.join(random.choice(string.ascii_lowercase) for _ in range(100))):
        self.key = key
        if any(char.isdigit() or char.isupper() for char in self.key):
            raise ValueError('wrong key')

    def encode(self, message):
        return shift(message, self.key, True)

    def decode(self, message):
        return shift(message, self.key, False)
