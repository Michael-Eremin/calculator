"""Function module for calculating the value by parsing the entire
expression string. """


from numexpr import evaluate
from numpy import round
from math import pi


# List to create a line for calculation.
lbl_screen_list = []

# List to create a string to display.
text_for_screen = []

# Operation arrays.
operations_to_manage = ['STR', '<<<', 'CE', '=']
operations_requiring_interpretation = [' 2√x', ' 3√x', ' L circle_r',
                                       ' S circle_r', ' V ball_r', ' 1/x', '^']


def calculate_by_line(expression_string: str) -> str:
    """Parses the given string and makes calculations."""
    try:
        result = evaluate(expression_string)
        return str(round(result, 4))
    except SyntaxError:
        return 'invalid string'
    except ZeroDivisionError:
        return 'division by zero'
    except TypeError:
        return 'operand not specified'


def make_screen_text(text_list: list) -> str:
    """Converts a list to a string for display."""
    text = ''.join(text_list)
    return text


def clear_text():
    """Removes content from the calculated list and screen list."""
    lbl_screen_list.clear()
    text_for_screen.clear()


def interpret_operation(act_btn: str) -> str:
    """Interprets the name of the operation buttons for the calculation."""
    if act_btn == '^':
        text_for_screen.append(act_btn)
        act_btn = '**'
        lbl_screen_list.append(act_btn)
        return make_screen_text(text_for_screen)
    elif act_btn == ' 1/x':
        lbl_screen_list.insert(0, '1/(')
        lbl_screen_list.append(')')
        text_for_screen.insert(0, '1/(')
        text_for_screen.append(')')
        return make_screen_text(text_for_screen)
    elif act_btn == ' 2√x':
        lbl_screen_list.insert(0, '(')
        lbl_screen_list.append(')**(1/2)')
        text_for_screen.insert(0, '(')
        text_for_screen.append(')2√x')
        return make_screen_text(text_for_screen)
    elif act_btn == ' 3√x':
        lbl_screen_list.insert(0, '(')
        lbl_screen_list.append(')**(1/3)')
        text_for_screen.insert(0, '(')
        text_for_screen.append(')3√x')
        return make_screen_text(text_for_screen)
    elif act_btn == ' L circle_r':
        lbl_screen_list.insert(0, '(')
        end_str = f')*2*{pi}'
        lbl_screen_list.append(end_str)
        text_for_screen.insert(0, '(')
        text_for_screen.append(')Lc_r')
        return make_screen_text(text_for_screen)
    elif act_btn == ' S circle_r':
        lbl_screen_list.insert(0, '(')
        end_str = f')**2*{pi}'
        lbl_screen_list.append(end_str)
        text_for_screen.insert(0, '(')
        text_for_screen.append(')Sc_r')
        return make_screen_text(text_for_screen)
    elif act_btn == ' V ball_r':
        lbl_screen_list.insert(0, '(')
        end_str = f')**3*{(4/3)*pi}'
        lbl_screen_list.append(end_str)
        text_for_screen.insert(0, '(')
        text_for_screen.append(')Vb_r')
        return make_screen_text(text_for_screen)


def value_lbl_screen_str(act_btn: str) -> str:
    """
    Gets activated button values and puts them to work
    >>> value_lbl_screen_str('3')
    '3'
    >>> value_lbl_screen_str('+')
    '3+'
    >>> value_lbl_screen_str('5')
    '3+5'
    >>> value_lbl_screen_str(' 3√x')
    '(3+5)3√x'
    >>> value_lbl_screen_str('=')
    '2.0'
    """
    if act_btn not in operations_to_manage \
            and act_btn not in operations_requiring_interpretation:
        lbl_screen_list.append(act_btn)
        text_for_screen.append(act_btn)
        return make_screen_text(text_for_screen)
    elif act_btn == '=':
        lbl_screen_str = ''.join(lbl_screen_list)
        text_for_screen.clear()
        text_for_screen.append(calculate_by_line(lbl_screen_str))
        return make_screen_text(text_for_screen)
    elif act_btn == 'CE':
        clear_text()
        return make_screen_text(text_for_screen)
    elif act_btn == '<<<':
        try:
            lbl_screen_list.pop()
            text_for_screen.pop()
            return make_screen_text(text_for_screen)
        except IndexError:
            return 'incorrect operation'
    elif act_btn in operations_requiring_interpretation:
        return interpret_operation(act_btn)

