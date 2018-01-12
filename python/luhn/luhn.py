class Luhn:
    def __init__(self, number):
        self.checknumber = str(number)[:-1].replace(' ', '')
        self.checkdigit = int(str(number)[-1])

    def addends(self):
        return Luhn.double_number(self.checknumber) + [self.checkdigit]

    def checksum(self):
        return sum(self.addends())

    def is_valid(self):
        if len(self.checknumber) < 1 or not all(char.isdigit() for char in self.checknumber) or self.checksum() % 10 != 0:
            return False
        return True

    @staticmethod
    def double_number(number):
        number = list(map(int, number))
        for counter, value in enumerate(number[::-1]):
            index = len(number) - counter - 1
            if counter % 2 == 0:
                value *= 2
                if value >= 10:
                    value -= 9
                number[index] = value
        return number
