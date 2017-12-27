class Luhn:
    def __init__(self, number):
        self.checknumber = int(str(number)[:-1])
        self.checkdigit = int(str(number)[-1])

    def addends(self):
        return Luhn.double_number(self.checknumber) + [self.checkdigit]

    def checksum(self):
        return sum(self.addends())

    @property
    def is_valid(self):
        return False if self.checksum() % 10 else True

    @staticmethod
    def create(number):
        return int(str(number) +
                   str((10 - sum(Luhn.double_number(number)) % 10) % 10))

    @staticmethod
    def double_number(number):
        number = list(map(int, str(number)))
        for counter, value in enumerate(number[::-1]):
            index = len(number) - counter - 1
            if counter % 2 == 0:
                value *= 2
                if value >= 10:
                    value -= 9
                number[index] = value
        return number
