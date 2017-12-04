from math import cos, sin, exp


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real, self.imaginary = real, imaginary

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def mul(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real, imaginary)

    def sub(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def div(self, other):
        real = (self.real * other.real + self.imaginary * other.imaginary)/(pow(other.real, 2) + pow(other.imaginary, 2))
        imaginary = (self.imaginary * other.real - self.real * other.imaginary)/(pow(other.real, 2) + pow(other.imaginary, 2))
        return ComplexNumber(real, imaginary)

    def abs(self):
        return pow(pow(self.real, 2) + pow(self.imaginary, 2), 1 / 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(cos(self.imaginary) * exp(self.real), round(sin(self.imaginary) * exp(self.real)))
