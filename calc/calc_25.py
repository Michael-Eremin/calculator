"""Graphing calculator program. The calculations are performed sequentially, one after the other."""
import tkinter as tk
from math import *
import tkinter.font as tkFont
from decimal import *


# Class 'tkinter' instance.
window = tk.Tk()
window.title('CALCULATOR')

# Window Options.
window.columnconfigure([0, 1, 2, 3], weight=1, minsize=130)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1, minsize=60)
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
                 [' L circle_r', ' S circle_r', ' V ball_r', '=']
                 ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
operations = ['+', '^', ' 2√x', ' 3√x', '-', '/', '*', ' L circle_r', ' S circle_r', ' V ball_r', ' 1/x']
operations_for_two_operands = ['+', '^', '-', '/', '*']
operations_for_first_operand = [' 2√x', ' 3√x', ' L circle_r', ' S circle_r', ' V ball_r', ' 1/x']

# Sequence of values of activated buttons for the First operand
first_operand_digits = []

# Sequence of values of activated buttons for the Next operand
next_operand_digits = []

# Values of activated buttons for the operation
operation_value = ['']

# Counting the Operation queue in the expression displayed on the screen
count_operations = [0]

# Counting the queue of the intermediate Result in the expression displayed on the screen
# count_result = [0]


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


def value_lbl_screen(row, col):
    """Screen display."""
    # For 'number'.
    if names_buttons[row][col] in numbers:
        activate_number_button(names_buttons[row][col])
    # For '='.
    elif names_buttons[row][col] == '=' and len(first_operand_digits) > 0:
        activate_equally_button(names_buttons[row][col])
    # For 'function_operator'.
    elif names_buttons[row][col] in operations:
        activate_operation_button(names_buttons[row][col])
    # For 'CE'.
    elif names_buttons[row][col] == 'CE':
        activate_ce_button()

# Format and location of buttons.
for i in range(len(names_buttons)):
    for j in range(len(names_buttons[i])):
        btn_buttons = tk.Button(
            master=window,
            relief=tk.RIDGE,
            borderwidth=3,
            text=names_buttons[i][j],
            font=fontExample,
            bg="GREEN",
            #Button activation.
            command=lambda row=i, col=j: value_lbl_screen(row, col)
        )
        btn_buttons.grid(row=i, column=j, sticky="nsew")
if __name__ == '__main__':

    window.mainloop()