class Phone:
    def __init__(self, number):
        number = ''.join(i for i in number if i.isdigit())
        if len(number) < 10 or len(number) > 11 or len(number) == 11 and number[0] != '1':
            raise ValueError('Invalid number')
        if len(number) == 11 and number[0] == '1':
            number = number[1:]
        if number[0] == '0' or number[0] == '1':
            raise ValueError('Area code does not start with 2-9')
        if number[3] == '0' or number[3] == '1':
            raise ValueError('Exchange code does not start with 2-9')
        self.number = number

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return '({}) {}-{}'.format(self.number[:3], self.number[3:6], self.number[6:])
