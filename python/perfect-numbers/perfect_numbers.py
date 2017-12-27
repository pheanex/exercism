def is_perfect(number):
    return sum(n for n in range(1, number // 2 + 1) if number % n == 0) == number
