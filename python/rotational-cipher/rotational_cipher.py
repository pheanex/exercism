from string import ascii_lowercase as lower
from string import ascii_uppercase as upper


def transpose(letter, key):
    if letter in lower:
        return lower[(lower.find(letter) + key) % len(lower)]
    if letter in upper:
        return upper[(upper.find(letter) + key) % len(upper)]
    return letter


def rotate(text, key):
    return ''.join(transpose(char, key) for char in text)
