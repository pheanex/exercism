class Triangle:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        if self.x <= 0 or self.y <= 0 or self.z <= 0 or\
           self.x + self.y <= self.z or\
           self.x + self.z <= self.y or\
           self.y + self.z <= self.x:
            raise TriangleError('Illegal values')

    def kind(self):
        if self.x == self.y == self.z:
            return 'equilateral'
        elif len({self.x, self.y, self.z}) == 2:
            return 'isosceles'
        else:
            return 'scalene'


class TriangleError(Exception):
    pass
