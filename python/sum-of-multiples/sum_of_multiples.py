def sum_of_multiples(n, multiples):
    numbers = set()
    for number in multiples:
        i = 1
        multiple = i * number
        while 0 < multiple < n:
            numbers.add(multiple)
            i += 1
            multiple = i * number

    return sum(numbers)
