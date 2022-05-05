"""Testing the 'calculate_by_line' function from the expression.py module."""
import doctest
from unittest import TestCase, main
from calc import expression





def load_tests(loader, tests, ignore, calc=None):
    tests.addTests(doctest.DocTestSuite(expression))
    return tests

class CalculatorTest(TestCase):
    def test_one_operation(self):
        self. assertEqual(expression.calculate_by_line('2+2'), '4')
        self. assertEqual(expression.calculate_by_line('2**2'), '4')
        self. assertEqual(expression.calculate_by_line('4**0.5'), '2.0')

    def test_priority(self):
        self. assertEqual(expression.calculate_by_line('2+2*5'), '12')
        self. assertEqual(expression.calculate_by_line('2+2*5/2-7*2'), '-7.0')

    def test_parentheses(self):
        self. assertEqual(expression.calculate_by_line('(2+2)*5'), '20')
        self. assertEqual(expression.calculate_by_line('((2+2)*5-2)/9'), '2.0')
        self. assertEqual(expression.calculate_by_line('(6-2)/2**2'), '1.0')

    def test_functions(self):
        self. assertEqual(expression.calculate_by_line('(2+2)*5'), '20')

    def test_incorrect_entry(self):
        with self.assertRaises(SyntaxError) as e:
            expression.calculate_by_line('55++')
            expression.calculate_by_line('')





if __name__ == '__main__':
    main()