def prime_factors(number):
    factors = []
    for i in range(2, number+1):
        while number % i == 0:
            factors.append(i)
            number //= i
        if number == 1:
            break
    return factors
