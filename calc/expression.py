"""The calculator calculates the value by parsing the entire string."""

import numexpr as ne

def calculate_by_line(expression_string: str) -> float:
    """Parses the given string and makes calculations."""
    result = ne.evaluate(expression_string)
    return result









if __name__ == '__main__':
    calculate_by_line('(1+2)/2')
