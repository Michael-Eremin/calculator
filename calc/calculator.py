"""Graphing calculator program. The calculations are performed sequentially, one after the other."""
import tkinter as tk
from math import *
import tkinter.font as tkFont
from decimal import *
from calc.expression import calculate_by_line

# Class 'tkinter' instance.
window = tk.Tk()

# Window Options.
window.title('CALCULATOR')
window.columnconfigure([0, 1, 2, 3], weight=1, minsize=130)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6,7], weight=1, minsize=60)
fontExample = tkFont.Font(family="Arial", size=18, weight="normal", slant="roman")
lbl_screen = tk.Label(master=window, font=fontExample, text='')
lbl_screen.grid(row=0, columnspan=4, sticky='nsew')

# Button markings
names_buttons = [[],
                 ['7', '8', '9', 'CE'],
                 ['4', '5', '6', '*'],
                 ['1', '2', '3', '/'],
                 ['0', '.', ' 1/x', '+'],
                 ['^', ' 2√x', ' 3√x', '-'],
                 [' L circle_r', ' S circle_r', ' V ball_r', '='],
                 ['STR', '(', ')', '<<<']
                 ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
operations = ['+', '^', ' 2√x', ' 3√x', '-', '/', '*', ' L circle_r', ' S circle_r', ' V ball_r', ' 1/x']
operations_for_two_operands = ['+', '^', '-', '/', '*']
operations_for_first_operand = [' 2√x', ' 3√x', ' L circle_r', ' S circle_r', ' V ball_r', ' 1/x']
operations_to_manage = ['STR', '<<<', 'CE', '=']
operations_requiring_interpretation = [' 2√x', ' 3√x', ' L circle_r', ' S circle_r', ' V ball_r', ' 1/x', '^']
operations_for_mode_str = ['STR', '(', ')', '<<<']

# Sequence of values of activated buttons for the First operand
first_operand_digits = []

# Sequence of values of activated buttons for the Next operand
next_operand_digits = []

# Values of activated buttons for the operation
operation_value = ['']

# Counting the Operation queue in the expression displayed on the screen
count_operations = [0]

# working mode:
#             throughout the line: mode[0] == 1;
#             successively: mode[0] == 0.
mode = [0]

# List to calculate in 'STR' mode.
lbl_screen_list = []


def check_process_status() -> list[str]:
    """Specifies the current status code.
    return:
    '_' == no values, is the first operand make;
    'result' == the result of the previous operation;
    '_F_of' == there is a first operand and a function for one operand (for first)
    '_F_ot' == there is a first operand and a function for two operands (for two)
    '_F_ot_N' == there is a first operand and a function for two operands and next operand
    """
    status = list()
    status.append('')
    if count_operations[0] == 0:
        status[0] = '_'
    elif first_operand_digits and not next_operand_digits:
        if count_operations[0] == 1 and operation_value[0] == '=':
            status[0] = 'result'
        # First choice of operation for one first operand
        elif count_operations[0] == 1 and operation_value[0] in operations_for_first_operand:
            status[0] = '_F_of'
        # Selecting the next operation that will run the first one
        elif count_operations[0] >= 2 and operation_value[0] in operations_for_first_operand:
            status[0] = '_F_of'
        # Selecting the next operation that will run the first one
        elif count_operations[0] >= 2 and operation_value[0] in operations_for_two_operands:
            status[0] = '_F_ot'
        # First choice of operation for two operands
        elif count_operations[0] == 1 and operation_value[0] in operations_for_two_operands:
            status[0] = '_F_ot'
        # Possible replacements for the first operation
        elif count_operations[0] >= 2 and operation_value[0] in operations_for_first_operand:
            status[0] = '_F_of'
        # Possible replacements for the first operation
        elif count_operations[0] >= 2 and operation_value[0] in operations_for_two_operands:
            status[0] = '_F_ot'
    elif next_operand_digits:
        status[0] = '_F_ot_N'
    return status


def calculate_result(operand_1: str, function_operator: str, operand_2=None) -> str:
    """Operations on numbers."""
    operand_1 = float(operand_1)
    if operand_2 != '':
        operand_2 = float(operand_2)
    if function_operator == '/':
        result_operation = operand_1 / operand_2
    if function_operator == '*':
        result_operation = operand_1 * operand_2
    elif function_operator == '+':
        result_operation = operand_1 + operand_2
    elif function_operator == '-':
        result_operation = operand_1 - operand_2
    elif function_operator == '^':
        result_operation = operand_1 ** operand_2
    elif function_operator == ' 2√x':
        result_operation = operand_1 ** float(1 / 2)
    elif function_operator == ' 3√x':
        result_operation = operand_1 ** float(1 / 3)
    elif function_operator == ' L circle_r':
        result_operation = float(2) * float(pi) * operand_1
    elif function_operator == ' S circle_r':
        result_operation = float(pi) * (operand_1 ** float(2))
    elif function_operator == ' V ball_r':
        result_operation = float(4/3) * float(pi) * (operand_1 ** float(3))
    elif function_operator == ' 1/x':
        result_operation = float(1) / operand_1
    return round(result_operation, 4)


def write_first_operand(act_btn):
    if act_btn != '.' or act_btn == '.' and '.' not in first_operand_digits:
        lbl_screen['text'] += act_btn
        first_operand_digits.extend(act_btn)


def write_next_operand(act_btn):
    if act_btn != '.' or act_btn == '.' and '.' not in next_operand_digits:
        lbl_screen['text'] += act_btn
        next_operand_digits.extend(act_btn)


def write_operation(act_btn):
    lbl_screen['text'] = lbl_screen['text'].replace(operation_value[0], '') + act_btn


def reset_status():
    count_operations[0] = 0
    operation_value[0] = ''
    first_operand_digits.clear()
    next_operand_digits.clear()


def call_calculation():
    operand_1 = ''.join(first_operand_digits)
    operand_2 = ''.join(next_operand_digits)
    function_operator = operation_value[0]
    intermediate_result = list()
    intermediate_result.append('')
    if function_operator == '/' and float(operand_2) == 0:
        reset_status()
        intermediate_result[0] = 'ERROR'
    elif function_operator == ' 1/x' and float(operand_1) == 0:
        reset_status()
        intermediate_result[0] = 'ERROR'
    else:
        intermediate_result[0] = calculate_result(operand_1, function_operator, operand_2)
        reset_status()
        first_operand_digits.extend(str(intermediate_result[0]))
    return intermediate_result[0]


def activate_equally_button(act_btn):
    """Activation of the button with the value of '='."""
    status = check_process_status()
    result = list()
    result.append(0)

    if status[0] == '_F_of' or status[0] == '_F_ot_N':
        result[0] = call_calculation()
        lbl_screen['text'] = str(result[0])
    count_operations[0] = + 1
    operation_value[0] = act_btn


def activate_number_button(act_btn):
    """Activation of the button with the value of the digit."""
    status = check_process_status()
    if status[0] != 'result':
        if status[0] == '_' and not operation_value[0]:
            write_first_operand(act_btn)
        elif status[0] == '_' and operation_value[0]:
            reset_status()
            write_first_operand(act_btn)
        elif status[0] == '_F_ot' or status[0] == '_F_ot_N':
            write_next_operand(act_btn)


def activate_operation_button(act_btn):
    """Button activation with function_operator value."""

    status = check_process_status()
    print('1status:', status)
    result = list()
    result.append(0)
    if status[0] == '_':
        write_operation(act_btn)
    elif status[0] == '_F_ot' or status[0] == 'result':
        write_operation(act_btn)
    elif status[0] == '_F_of' or status[0] == '_F_ot_N':
        result[0] = call_calculation()
        lbl_screen['text'] = str(result[0]) + act_btn
    count_operations[0] = + 1
    operation_value[0] = act_btn
    print('status num:', status[0])
    print('res:', result)


def activate_ce_button():
    """Activation of the button with the value of 'CE'."""
    reset_status()
    lbl_screen['text'] = ''


def interpret_operation(act_btn):
    if act_btn == '^':
        lbl_screen['text'] += act_btn
        act_btn = '**'
        lbl_screen_list.append(act_btn)
    elif act_btn == ' 1/x':
        lbl_screen_list.insert(0, '1/(')
        lbl_screen_list.append(')')
        lbl_screen['text'] = '1/(' + lbl_screen['text'] + ')'
    elif act_btn == ' 2√x':
        lbl_screen_list.insert(0, '(')
        lbl_screen_list.append(')**(1/2)')
        lbl_screen['text'] = '(' + lbl_screen['text'] + ')2√x'
    elif act_btn == ' 3√x':
        lbl_screen_list.insert(0, '(')
        lbl_screen_list.append(')**(1/3)')
        lbl_screen['text'] = '(' + lbl_screen['text'] + ')3√x'
    elif act_btn == ' L circle_r':
        lbl_screen_list.insert(0, '(')
        end_str = f')*2*{pi}'
        lbl_screen_list.append(end_str)
        lbl_screen['text'] = '(' + lbl_screen['text'] + ')Lc_r'
    elif act_btn == ' S circle_r':
        lbl_screen_list.insert(0, '(')
        end_str = f')**2*{pi}'
        lbl_screen_list.append(end_str)
        lbl_screen['text'] = '(' + lbl_screen['text'] + ')Sc_r'
    elif act_btn == ' V ball_r':
        lbl_screen_list.insert(0, '(')
        end_str = f')**3*{(4/3)*pi}'
        lbl_screen_list.append(end_str)
        lbl_screen['text'] = '(' + lbl_screen['text'] + ')Vb_r'


def value_lbl_screen_str(act_btn):
    if act_btn not in operations_to_manage and act_btn not in operations_requiring_interpretation:
        lbl_screen['text'] += act_btn
        lbl_screen_list.append(act_btn)
        print('lbl_screen_list', lbl_screen_list)
    elif act_btn == '=':
        lbl_screen_str = ''.join(lbl_screen_list)
        result = calculate_by_line(lbl_screen_str)
        lbl_screen['text'] = result
    elif act_btn == 'CE':
        lbl_screen['text'] = ''
        lbl_screen_list.clear()
    elif act_btn == '<<<':
        lbl_screen_list.pop()
        print('lbl_screen_list', lbl_screen_list)
        lbl_screen['text'] = ''.join(lbl_screen_list)
    elif act_btn in operations_requiring_interpretation:
        interpret_operation(act_btn)


def value_lbl_screen(act_btn):
    """Screen display."""
    # For 'number'.
    if act_btn in numbers:
        activate_number_button(act_btn)
    # For '='.
    elif act_btn == '=' and len(first_operand_digits) > 0:
        activate_equally_button(act_btn)
    # For 'function_operator'.
    elif act_btn in operations:
        activate_operation_button(act_btn)
    # For 'CE'.
    elif act_btn == 'CE':
        activate_ce_button()


def make_widget_str():
    for i in range(7, 8):
        for j in range(0,1):
            if mode[0] == 1:
                color_mode = "#FFF38F"
                btn_buttons(i, j, color_mode)
            else:
                color_mode = "#8FFFA2"
                btn_buttons(i, j, color_mode)


def make_widget_mode_str():
    for i in range(7, 8):
        for j in range(1, 4):
            if mode[0] == 1:
                color_mode = "#01C624"
                btn_buttons(i, j, color_mode)
            else:
                color_mode = "#8FFFA2"
                btn_buttons(i, j, color_mode)


def select_mode(row, col):
    act_btn = names_buttons[row][col]
    print('mode', mode[0])
    if act_btn == 'STR':
        if mode[0] == 1:
            lbl_screen['text'] = ''
            lbl_screen_list.clear()
            mode[0] = 0
        else:
            activate_ce_button()
            mode[0] = 1
        make_widget_str()
        make_widget_mode_str()
    if mode[0] == 1:
        value_lbl_screen_str(act_btn)
    else:
        value_lbl_screen(act_btn)


def btn_buttons(i, j, color_mode):

    btn_buttons = tk.Button(
        master=window,
        relief=tk.RIDGE,
        borderwidth=3,
        text=names_buttons[i][j],
        font=fontExample,
        bg=color_mode,
        activebackground='#FF8FF7',
        # Button activation.
        command=lambda row=i, col=j: select_mode(row, col)
    )
    btn_buttons.grid(row=i, column=j, sticky="nsew")


def make_widget_not_mode_str():
    for i in range(0,7):
        for j in range(len(names_buttons[i])):
            color_mode = "#01C624"
            btn_buttons(i, j, color_mode)


def make_widget():
    make_widget_not_mode_str()
    make_widget_str()
    make_widget_mode_str()


if __name__ == '__main__':
    make_widget()
    window.mainloop()
