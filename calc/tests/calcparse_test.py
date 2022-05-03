"""Testing the 'calculate_by_line' function from the calc_parse.py module."""
from unittest import TestCase, main
from calc.calc_parse import calculate_by_line

class CalculatorTest(TestCase):
    def test_one_operation(self):
        self. assertEqual(calculate_by_line('2+2'), 4)
        self. assertEqual(calculate_by_line('2**2'), 4)
        self. assertEqual(calculate_by_line('4**0.5'), 2)

    def test_priority(self):
        self. assertEqual(calculate_by_line('2+2*5'), 12)
        self. assertEqual(calculate_by_line('2+2*5/2-7*2'), -7)
    def test_parentheses(self):
        self. assertEqual(calculate_by_line('(2+2)*5'), 20)
        self. assertEqual(calculate_by_line('((2+2)*5-2)/9'), 2)
        self. assertEqual(calculate_by_line('(6-2)/2**2'), 1.0)




if __name__ == '__main__':
    main()