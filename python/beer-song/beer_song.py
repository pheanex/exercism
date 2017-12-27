def bottles(n):
    if n == 0:
        return "no more bottles"
    elif n == 1:
        return "1 bottle"
    else:
        return "{} bottles".format(n)


def verse(count):
    nr_less = bottles(count - 1)
    line2 = 'Take one down and pass it around'
    if count == 0:
        nr_less = bottles(99)
        line2 = 'Go to the store and buy some more'
    elif count == 1:
        line2 = 'Take it down and pass it around'
    text = '{nr} of beer on the wall, {nr_} of beer.\n{line2}, {nr_less} of beer on the wall.\n'
    return text.format(nr=bottles(count).capitalize(), nr_=bottles(count), line2=line2, nr_less=nr_less)


def song(start, stop=0):
    return ''.join(verse(i) + '\n' for i in range(start, stop - 1, -1))
