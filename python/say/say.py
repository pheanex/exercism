simple_names = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
decadic_names = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
mill_names = ['thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion',
              'septillion', 'octillion', 'nonillion', 'decillion']


def say(number):
    number = int(number)

    def say_under_20(number):
        return simple_names[number]

    def say_under_100(number):
        if number < 20:
            return say_under_20(number)
        else:
            if number % 10 == 0:
                return decadic_names[number % 100 // 10]
            else:
                return decadic_names[number % 100 // 10] + "-" + say_under_20(number % 10)

    def say_under_1000(number):
        if number < 100:
            return say_under_100(number)
        else:
            if number % 100 == 0:
                return say_under_20(number // 100) + " hundred"
            else:
                return say_under_20(number // 100) + " hundred and " + say_under_100(number % 100)

    if not 0 <= number <= 999999999999:
        raise AttributeError("Value not in range")

    if number == 0:
        return "zero"

    i = number
    blocks = []
    while i > 0:
        blocks.insert(0, i % 1000)
        i //= 1000

    number_name = str(say_under_1000(blocks[-1]))
    if number > 999 and 0 < blocks[-1] < 100:
        number_name = "and " + number_name

    for mill_name, block in zip(mill_names, blocks[::-1][1:]):
        if block != 0:
            if number_name == "":
                number_name = say_under_1000(block) + " " + mill_name
            else:
                number_name = say_under_1000(block) + " " + mill_name + " " + number_name
    return number_name
