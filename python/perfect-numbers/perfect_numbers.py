def is_perfect(number):
    divisors = [n for n in range(1, int(number/2+1)) if not number % n]
    if sum(divisors) == number:
        return True
    return False
