# -*- coding: utf-8 -*-
from itertools import groupby


def encode(string):
    return_string = ''
    for k, g in groupby(string):
        group = list(g)
        if len(group) > 1:
            return_string += str(len(group)) + k
        else:
            return_string += k
    return return_string


def decode(string):
    number = return_string = ''
    for current in string:
        if current.isdigit():
            number += current
        else:
            if number.isdigit():
                return_string += int(number)*current
            else:
                return_string += current
            number = ''
    return return_string
