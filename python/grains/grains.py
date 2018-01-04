def on_square(fieldnumber):
    if not 0 < fieldnumber < 65:
        raise ValueError('Invalid fieldnumber')
    return 2 ** (fieldnumber - 1)


def total_after(fieldnumber):
    if not 0 < fieldnumber < 65:
        raise ValueError('Invalid fieldnumber')
    return sum(on_square(field) for field in range(1, fieldnumber + 1))
