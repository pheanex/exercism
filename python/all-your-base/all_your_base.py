def rebase(from_base, digits, to_base):
    if from_base < 2:
        raise ValueError
    if not all(0 <= digit < from_base for digit in digits):
        raise ValueError
    if to_base < 2:
        raise ValueError

    sum = 0
    for index, digit in enumerate(digits, start=1):
        power = len(digits) - index
        sum += digit * pow(from_base, power)

    digits = []
    while sum:
        digits.append(sum % to_base)
        sum //= to_base

    return digits[::-1]
