def factor_generator(number):
    if number > 1:
        yield 1
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            yield divisor
            if divisor * divisor != number:
                yield number // divisor


def classify(number):
    if number < 1:
        raise ValueError('Number not in range')
    sum_of_factors = sum(factor_generator(number))
    if sum_of_factors == number:
        return 'perfect'
    if sum_of_factors > number:
        return 'abundant'
    return 'deficient'
