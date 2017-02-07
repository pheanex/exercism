def sieve(number):
    numbers = list(range(2, number + 1))
    primes = []
    while numbers:
        prime = numbers[0]
        primes += [prime]
        numbers = [number for number in numbers if number % prime != 0]

    return primes
