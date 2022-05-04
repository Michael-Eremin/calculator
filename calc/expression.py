"""The calculator calculates the value by parsing the entire string."""

import numexpr as ne
import numpy as np
from math import pi


# List to calculate in 'STR' mode.
lbl_screen_list = []
text_for_screen = []
operations_to_manage = ['STR', '<<<', 'CE', '=']
operations_requiring_interpretation = [' 2√x', ' 3√x', ' L circle_r', ' S circle_r', ' V ball_r', ' 1/x', '^']

def calculate_by_line(expression_string: str) -> float:
    """Parses the given string and makes calculations."""
    result = ne.evaluate(expression_string)
    return str(np.round(result, 4))


def make_screen_text(text_for_screen):
    text = ''.join(text_for_screen)
    return text


def interpret_operation(act_btn):
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


def value_lbl_screen_str(act_btn):
    if act_btn not in operations_to_manage and act_btn not in operations_requiring_interpretation:
        lbl_screen_list.append(act_btn)
        text_for_screen.append(act_btn)
        return make_screen_text(text_for_screen)
    elif act_btn == '=':
        lbl_screen_str = ''.join(lbl_screen_list)
        text_for_screen.clear()
        text_for_screen.append(calculate_by_line(lbl_screen_str))
        return make_screen_text(text_for_screen)
    elif act_btn == 'CE':
        lbl_screen_list.clear()
        text_for_screen.clear()
        return make_screen_text(text_for_screen)
    elif act_btn == '<<<':
        lbl_screen_list.pop()
        text_for_screen.pop()
        return make_screen_text(text_for_screen)
    elif act_btn in operations_requiring_interpretation:
        return interpret_operation(act_btn)








if __name__ == '__main__':
    calculate_by_line('(1+2)/2')
