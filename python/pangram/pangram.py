# -*- coding: utf-8 -*-
import string

char_occurrence_count = {}


def is_pangram(sentence):
    for char in sentence:
        char = char.lower()
        if char in string.ascii_lowercase:
            char_occurrence_count[char] = 1

    for char in string.ascii_lowercase:
        if char not in char_occurrence_count or char_occurrence_count[char] == 0:
            return False

    return True
