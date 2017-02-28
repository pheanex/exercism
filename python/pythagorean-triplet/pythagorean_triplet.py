def is_triplet(a, b, c):
    return a**2 + b**2 == c**2


def primitive_triplets(number):
    print("I don't understand the exercise ...")


def triplets_in_range(start, stop):
    return {primitive_triplets(x) for x in range(start, stop+1)}
