class Phone:
    def __init__(self, number):
        number = ''.join(i for i in number if i.isdigit())
        if len(number) < 10 or len(number) == 11 and not number[0] == '1' or len(number) > 11:
            number = '0000000000'
        elif len(number) == 11 and number[0] == '1':
            number = number[-10:]
        self.number = number

    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return '({}) {}-{}'.format(self.number[:3], self.number[3:6], self.number[6:])
