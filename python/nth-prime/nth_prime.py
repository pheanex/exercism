from math import sqrt, ceil
from functools import lru_cache


@lru_cache(maxsize=None)
def is_prime(number):
    for i in range(2, ceil(sqrt(number+1))):
        if number % i == 0:
            return False
    return True


@lru_cache(maxsize=None)
def nth_prime(position):
    number = 2
    prime_count = 0
    while True:
        if is_prime(number):
            prime_count += 1
            if prime_count == position:
                return number
        number += 1
