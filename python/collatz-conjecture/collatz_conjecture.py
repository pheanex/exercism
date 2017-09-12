def collatz_steps(number, count=0):
    if number < 1:
        return None
    while number != 1:
        count += 1
        number = number/2 if number%2 == 0 else 3*number + 1
    return count
