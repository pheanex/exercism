convert = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }


def numeral(number):
    roman = ""
    for i in [10**i for i in range(0, 4)][::-1]:
        floordiv = number // i
        if 0 < floordiv < 4:
            roman += floordiv*convert[i]
        elif floordiv in (4, 9):
            roman += convert[i]+convert[(floordiv+1)*i]
        elif 4 < floordiv < 9:
            roman += convert[5*i] + (floordiv-5)*convert[i]
        number -= floordiv*i

    return roman
