def classify(number):
    if number < 1:
        raise ValueError('Number not in range')
    sum_of_factors = sum(n for n in range(1, number // 2 + 1) if number % n == 0)
    if sum_of_factors == number:
        return 'perfect'
    if sum_of_factors > number:
        return 'abundant'
    return 'deficient'
