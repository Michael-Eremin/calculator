"""Testing the 'calculate_result' function from the one_action.py module."""
import doctest
from unittest import TestCase, main
from calc import one_action


def load_tests(loader, tests, ignore, calc=None):
    tests.addTests(doctest.DocTestSuite(one_action))
    return tests


class CalculatorTest(TestCase):
    def test_one_operation(self):
        self. assertEqual(one_action.calculate_result('2', '+', '2'), '4.0')
        self. assertEqual(one_action.calculate_result('4', ' 2√x', ''), '2.0')
        self.assertEqual(one_action.calculate_result('4', '^', '2'), '16.0')


if __name__ == '__main__':
    main()