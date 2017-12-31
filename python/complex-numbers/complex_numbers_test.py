import unittest

import math

from complex_numbers import ComplexNumber


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0


class ComplexNumbersTest(unittest.TestCase):

    def test_add_purely_real_numbers(self):
        first_input = ComplexNumber(1, 0)
        second_input = ComplexNumber(2, 0)
        self.assertEqual(first_input.add(second_input).real, 3)
        self.assertEqual(first_input.add(second_input).imaginary, 0)

    def test_add_purely_imaginary_numbers(self):
        first_input = ComplexNumber(0, 1)
        second_input = ComplexNumber(0, 2)
        self.assertEqual(first_input.add(second_input).real, 0)
        self.assertEqual(first_input.add(second_input).imaginary, 3)

    def test_add_numbers_with_real_and_imaginary_part(self):
        first_input = ComplexNumber(1, 2)
        second_input = ComplexNumber(3, 4)
        self.assertEqual(first_input.add(second_input).real, 4)
        self.assertEqual(first_input.add(second_input).imaginary, 6)

    def test_subtract_purely_real_numbers(self):
        first_input = ComplexNumber(1, 0)
        second_input = ComplexNumber(2, 0)
        self.assertEqual(first_input.sub(second_input).real, -1)
        self.assertEqual(first_input.sub(second_input).imaginary, 0)

    def test_subtract_purely_imaginary_numbers(self):
        first_input = ComplexNumber(0, 1)
        second_input = ComplexNumber(0, 2)
        self.assertEqual(first_input.sub(second_input).real, 0)
        self.assertEqual(first_input.sub(second_input).imaginary, -1)

    def test_subtract_numbers_with_real_and_imaginary_part(self):
        first_input = ComplexNumber(1, 2)
        second_input = ComplexNumber(3, 4)
        self.assertEqual(first_input.sub(second_input).real, -2)
        self.assertEqual(first_input.sub(second_input).imaginary, -2)

    def test_multiply_purely_real_numbers(self):
        first_input = ComplexNumber(1, 0)
        second_input = ComplexNumber(2, 0)
        self.assertEqual(first_input.mul(second_input).real, 2)
        self.assertEqual(first_input.mul(second_input).imaginary, 0)

    def test_multiply_purely_imaginary_numbers(self):
        first_input = ComplexNumber(0, 1)
        second_input = ComplexNumber(0, 2)
        self.assertEqual(first_input.mul(second_input).real, -2)
        self.assertEqual(first_input.mul(second_input).imaginary, 0)

    def test_multiply_numbers_with_real_and_imaginary_part(self):
        first_input = ComplexNumber(1, 2)
        second_input = ComplexNumber(3, 4)
        self.assertEqual(first_input.mul(second_input).real, -5)
        self.assertEqual(first_input.mul(second_input).imaginary, 10)

    def test_divide_purely_real_numbers(self):
        input_number = ComplexNumber(1.0, 0.0)
        expected = ComplexNumber(0.5, 0.0)
        divider = ComplexNumber(2.0, 0.0)
        self.assertEqual(input_number.div(divider).real, expected.real)
        self.assertEqual(input_number.div(divider).imaginary,
                         expected.imaginary)

    def test_divide_purely_imaginary_numbers(self):
        input_number = ComplexNumber(0, 1)
        expected = ComplexNumber(0.5, 0)
        divider = ComplexNumber(0, 2)
        self.assertEqual(input_number.div(divider).real, expected.real)
        self.assertEqual(input_number.div(divider).imaginary,
                         expected.imaginary)

    def test_divide_numbers_with_real_and_imaginary_part(self):
        input_number = ComplexNumber(1, 2)
        expected = ComplexNumber(0.44, 0.08)
        divider = ComplexNumber(3, 4)
        self.assertEqual(input_number.div(divider).real, expected.real)
        self.assertEqual(input_number.div(divider).imaginary,
                         expected.imaginary)

    def test_absolute_value_of_a_positive_purely_real_number(self):
        self.assertEqual(ComplexNumber(5, 0).abs(), 5)

    def test_absolute_value_of_a_negative_purely_real_number(self):
        self.assertEqual(ComplexNumber(-5, 0).abs(), 5)

    def test_absolute_value_of_imaginary_number_positive_imaginary_part(self):
        self.assertEqual(ComplexNumber(0, 5).abs(), 5)

    def test_absolute_value_of_imaginary_number_negative_imaginary_part(self):
        self.assertEqual(ComplexNumber(0, -5).abs(), 5)

    def test_absolute_value_of_a_number_with_real_and_imaginary_part(self):
        self.assertEqual(ComplexNumber(3, 4).abs(), 5)

    def test_conjugate_a_purely_real_number(self):
        input_number = ComplexNumber(5, 0)
        expected = ComplexNumber(5, 0)
        self.assertEqual(input_number.conjugate().real, expected.real)
        self.assertEqual(input_number.conjugate().imaginary,
                         expected.imaginary)

    def test_conjugate_a_purely_imaginary_number(self):
        input_number = ComplexNumber(0, 5)
        expected = ComplexNumber(0, -5)
        self.assertEqual(input_number.conjugate().real, expected.real)
        self.assertEqual(input_number.conjugate().imaginary,
                         expected.imaginary)

    def test_conjugate_a_number_with_real_and_imaginary_part(self):
        input_number = ComplexNumber(1, 1)
        expected = ComplexNumber(1, -1)
        self.assertEqual(input_number.conjugate().real, expected.real)
        self.assertEqual(input_number.conjugate().imaginary,
                         expected.imaginary)

    def test_real_part_of_a_purely_real_number(self):
        input_number = ComplexNumber(1, 0)
        self.assertEqual(input_number.real, 1)

    def test_real_part_of_a_purely_imaginary_number(self):
        input_number = ComplexNumber(0, 1)
        self.assertEqual(input_number.real, 0)

    def test_real_part_of_a_number_with_real_and_imaginary_part(self):
        input_number = ComplexNumber(1, 2)
        self.assertEqual(input_number.real, 1)

    def test_imaginary_part_of_a_purely_real_number(self):
        input_number = ComplexNumber(1, 0)
        self.assertEqual(input_number.imaginary, 0)

    def test_imaginary_part_of_a_purely_imaginary_number(self):
        input_number = ComplexNumber(0, 1)
        self.assertEqual(input_number.imaginary, 1)

    def test_imaginary_part_of_a_number_with_real_and_imaginary_part(self):
        input_number = ComplexNumber(1, 2)
        self.assertEqual(input_number.imaginary, 2)

    def test_eulers_identity_formula(self):
        input_number = ComplexNumber(0, math.pi)
        expected = ComplexNumber(-1, 0)
        self.assertEqual(input_number.exp().real, expected.real)
        self.assertEqual(input_number.exp().imaginary, expected.imaginary)

    def test_exponential_of_0(self):
        input_number = ComplexNumber(0, 0)
        expected = ComplexNumber(1, 0)
        self.assertEqual(input_number.exp().real, expected.real)
        self.assertEqual(input_number.exp().imaginary, expected.imaginary)

    def test_exponential_of_a_purely_real_number(self):
        input_number = ComplexNumber(1, 0)
        expected = ComplexNumber(math.e, 0)
        self.assertEqual(input_number.exp().real, expected.real)
        self.assertEqual(input_number.exp().imaginary, expected.imaginary)


if __name__ == '__main__':
    unittest.main()
