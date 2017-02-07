def largest_product(string, length):
    if length == 0:
        return 1
    if not string or length < 0 or len(string) < length:
        raise ValueError()

    max_product = 0
    for index in range(len(string)-length+1):
        product = 1
        for digit in map(int, string[index:index+length]):
            product *= digit
        if product > max_product:
            max_product = product
    return max_product
