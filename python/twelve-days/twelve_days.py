sentence = [("first", "a Partridge in a Pear Tree"),
            ("second", "two Turtle Doves"),
            ("third", "three French Hens"),
            ("fourth", "four Calling Birds"),
            ("fifth", "five Gold Rings"),
            ("sixth", "six Geese-a-Laying"),
            ("seventh", "seven Swans-a-Swimming"),
            ("eighth", "eight Maids-a-Milking"),
            ("ninth", "nine Ladies Dancing"),
            ("tenth", "ten Lords-a-Leaping"),
            ("eleventh", "eleven Pipers Piping"),
            ("twelfth", "twelve Drummers Drumming")]


def verse(nr):
    if nr > 1:
        presents = ', '.join([sentence[i][1] for i in range(nr - 1, 0, -1)]) + ', and ' + sentence[0][1]
    else:
        presents = ', '.join([sentence[i][1] for i in range(nr - 1, -1, -1)])
    return 'On the {} day of Christmas my true love gave to me, {}.\n'.format(sentence[nr-1][0], presents)


def verses(start, stop):
    return '\n'.join([verse(i) for i in range(start, stop+1)]) + '\n'


def sing():
    return verses(1, 12)
