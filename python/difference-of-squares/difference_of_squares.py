def square_of_sum(number):
    return sum(range(1, number + 1)) ** 2


def sum_of_squares(number):
    sqsum = 0
    for i in range(1, number + 1):
        sqsum += i ** 2
    return sqsum


def difference(number):
    return square_of_sum(number) - sum_of_squares(number)
