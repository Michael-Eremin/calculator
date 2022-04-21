'''Graphing calculator program. The calculations are performed sequentially, one after the other.'''
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

# Sequence of values of activated buttons for the First operand
first_operand_digits = []

# Values of activated buttons for the operation
operation_value = []

# Sequence of values of activated buttons for the Next operand
next_operand_digits = []

# Counting the Operation queue in the expression displayed on the screen
count_operations = [0]

# Counting the queue of the intermediate Result in the expression displayed on the screen
count_result = []


def operation_result (operand_1, function_operator, operand_2=None):
    '''Operations on numbers.'''
    result_operation = 0
    operand_1 = Decimal(operand_1)
    if not operand_2 is None:
        operand_2 = Decimal(operand_2)
    if function_operator == '/':
        if operand_2 == 0:
            result_operation = 'error'
            return "%s" % result_operation
        else:
            result_operation = operand_1 / operand_2
            return "%.2f" % round(result_operation, 2)
    if function_operator == '*':
        result_operation = operand_1 * operand_2
    elif function_operator == '+':
        result_operation = operand_1 + operand_2
    elif function_operator == '-':
        result_operation = operand_1 - operand_2
    elif function_operator == '^':
        result_operation = operand_1 ** operand_2
    elif function_operator == ' 2√x':
        result_operation = operand_1 ** Decimal(1 / 2)
    elif function_operator == ' 3√x':
        result_operation = operand_1 ** Decimal(1 / 3)
    elif function_operator == ' L circle_r':
        result_operation = Decimal(2) * Decimal(pi) * operand_1
    elif function_operator == ' S circle_r':
        result_operation = Decimal(pi) * (operand_1 ** Decimal(2))
    elif function_operator == ' V ball_r':
        result_operation = Decimal(4/3) * Decimal(pi) * (operand_1 ** Decimal(3))
    elif function_operator == ' 1/x':
        result_operation = Decimal(1) / operand_1
    return "%.2f" % round(result_operation, 2)


def activate_number_button(act_btn):
    '''Activation of the button with the value of the digit.'''
    if len(count_result) == 0:
        lbl_screen['text'] += act_btn
        if count_operations[0] == 0:
            first_operand_digits.extend(act_btn)
        else:
            next_operand_digits.extend(act_btn)
    else:
        if operation_value[0] == '=':
            lbl_screen['text'] = ''
            lbl_screen['text'] += act_btn
            operation_value.clear()
            first_operand_digits.clear()
            first_operand_digits.extend(act_btn)
            count_result.clear()
        else:
            lbl_screen['text'] += act_btn
            if count_operations[0] == 0:
                first_operand_digits.extend(act_btn)
            elif count_operations[0] >= 1:
                next_operand_digits.extend(act_btn)


def activate_equally_button(act_btn):
    '''Activation of the button with the value of '='.'''
    if operation_value[0] not in [' 2√x', ' 3√x', ' L circle_r', ' S circle_r', ' V ball_r', ' 1/x']:
        operand_1 = Decimal(''.join(first_operand_digits))
        operand_2 = Decimal(''.join(next_operand_digits))
        func_oper = operation_value[0]
        first_operand_digits.clear()
        next_operand_digits.clear()
        lbl_screen['text'] = str(operation_result(operand_1, func_oper, operand_2))

        if count_operations[0] <= 1:
            first_operand_digits.extend(str(lbl_screen['text']))
            operation_value.clear()
            operation_value.append(act_btn)
        else:
            first_operand_digits.extend(lbl_screen['text'])

        operation_value.clear()
        operation_value.append(act_btn)
        count_operations[0] = 0

    else:
        operand_1 = Decimal(''.join(first_operand_digits))
        func_oper = operation_value[0]
        first_operand_digits.clear()
        next_operand_digits.clear()
        lbl_screen['text'] = str(operation_result(operand_1, func_oper))
        first_operand_digits.extend(str(lbl_screen['text']))
        operation_value.clear()
        operation_value.append(act_btn)


def activate_operation_button(act_btn):
    '''Button activation with function_operator value.'''
    if count_operations[0] == 0:
        operation_value.clear()
        operation_value.append(act_btn)
        lbl_screen['text'] = act_btn



    if count_operations[0] == 1:
        operation_value.clear()
        operation_value.append(act_btn)
        lbl_screen['text'] = act_btn
    elif count_operations[0] > 1:
        if len(next_operand_digits) == 0:
            operation_value.clear()
            operation_value.append(act_btn)
            lbl_screen['text'] += act_btn
        else:
            operand_1 = Decimal(''.join(first_operand_digits))
            operand_2 = Decimal(''.join(next_operand_digits))
            func_oper = operation_value[0]
            first_operand_digits.clear()
            next_operand_digits.clear()
            operation_value.clear()
            operation_value.append(act_btn)
            if func_oper == '/' and operand_2 == 0:
                lbl_screen['text'] = 'error'
                count_result.clear()
                count_operations[0] = 0
                operation_value.clear()
                first_operand_digits.clear()
                next_operand_digits.clear()
            else:
                intermediate_result = operation_result(operand_1, func_oper, operand_2)
                first_operand_digits.extend(intermediate_result)
                lbl_screen['text'] = intermediate_result + act_btn


def activate_ce_button():
    '''Activation of the button with the value of 'CE'.'''
    count_result.clear()
    count_operations[0] = 0
    operation_value.clear()
    first_operand_digits.clear()
    next_operand_digits.clear()
    lbl_screen['text'] = ''


def value_lbl_screen(row, col):
    '''Screen display.'''
    # For 'number'.
    if names_buttons[row][col] in numbers:
        activate_number_button(names_buttons[row][col])
    # For '='.
    elif names_buttons[row][col] == '=' and len(first_operand_digits) > 0:
        count_result.extend('result')
        activate_equally_button(names_buttons[row][col])
    # For 'function_operator'.
    elif names_buttons[row][col] in operations:
        count_operations[0] += 1
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