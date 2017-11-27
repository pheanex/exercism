def rebase(from_base, digits, to_base):
    if from_base < 2:
        raise ValueError
    if any(digit for digit in digits if digit < 0 or digit >= from_base):
        raise ValueError
    if to_base < 2:
        raise ValueError

    number_length = len(digits)
    sum = 0
    for index, digit in enumerate(digits, start=1):
        power = number_length - index
        sum += digit * pow(from_base, power)

    digits = []
    while sum:
        quotient, remainder = divmod(sum, to_base)
        digits.append(remainder)
        sum = quotient
    return digits[::-1]
