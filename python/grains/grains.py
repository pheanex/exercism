def on_square(fieldnumber):
    return 2**(fieldnumber-1)


def total_after(fieldnumber):
    grainsum = 0
    for field in range(1, fieldnumber+1):
        grainsum += on_square(field)
    return grainsum
