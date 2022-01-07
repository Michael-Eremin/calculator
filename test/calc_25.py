import tkinter as tk
from math import *
import tkinter.font as tkFont



window = tk.Tk()
window.title('CALCULATOR')

window.columnconfigure([0, 1, 2, 3], weight=1, minsize=130)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1, minsize=60)

fontExample = tkFont.Font(family="Arial", size=18, weight="normal", slant="roman")

lbl_screen = tk.Label(master=window, font=fontExample, text='')
lbl_screen.grid(row=0, columnspan=4, sticky='nsew')



btn_buttons = tk.Button(master=window)

names_buttons = [[],
                 ['7', '8', '9', 'CE'],
                 ['4', '5', '6', '*'],
                 ['1', '2', '3', '/'],
                 ['0', '.', ' 1/x', '+'],
                 ['^', ' 2√x', ' 3√x', '-'],
                 [' L circle_r', ' S circle_r', ' V ball_r', '=']
                 ]

count_operations = [0]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
operations = ['+', '^', ' 2√x', ' 3√x', '-', '/', '*', ' L circle_r', ' S circle_r', ' V ball_r', ' 1/x']
nb_oper_1 = []
nb_operation = []
nb_oper_2 = []
count_result = []


def operation_result (oper_1, func_oper, oper_2=None):
    result_operation = 0
    if func_oper == '/':
        if oper_2 == 0:
            result_operation = 'error'
            return "%s" % result_operation
        else:
            result_operation = oper_1 / oper_2
            return "%.2f" % round(result_operation, 2)
    if func_oper == '*':
        result_operation = oper_1 * oper_2
    elif func_oper == '+':
        result_operation = oper_1 + oper_2
    elif func_oper == '-':
        result_operation = oper_1 - oper_2
    elif func_oper == '^':
        result_operation = oper_1 ** oper_2
    elif func_oper == ' 2√x':
        result_operation = oper_1 ** (1/2)
    elif func_oper == ' 3√x':
        result_operation = oper_1 ** (1/3)
    elif func_oper == ' L circle_r':
        result_operation = 2 * pi * oper_1
    elif func_oper == ' S circle_r':
        result_operation = pi * (oper_1 ** 2)
    elif func_oper == ' V ball_r':
        result_operation = ((4/3) * pi * (oper_1 ** 3))
    elif func_oper == ' 1/x':
        result_operation = 1/oper_1

    return "%.2f" % round(result_operation, 2)


def value_lbl_screen(row, col):
    if names_buttons[row][col] in numbers:
        if len(count_result) == 0:
            lbl_screen['text'] += (names_buttons[row][col])
            if count_operations[0] == 0:
                nb_oper_1.extend(names_buttons[row][col])

            else:
                nb_oper_2.extend(names_buttons[row][col])

        else:
            if nb_operation[0] == '=':
                lbl_screen['text'] = ''
                lbl_screen['text'] += (names_buttons[row][col])
                nb_operation.clear()
                nb_oper_1.clear()
                nb_oper_1.extend(names_buttons[row][col])
                count_result.clear()

            else:
                lbl_screen['text'] += (names_buttons[row][col])
                if count_operations[0] == 0:
                    nb_oper_1.extend(names_buttons[row][col])

                elif count_operations[0] == 1:
                    nb_oper_2.extend(names_buttons[row][col])

                elif count_operations[0] > 1:
                    nb_oper_2.extend(names_buttons[row][col])


    elif names_buttons[row][col] == '=' and len(nb_oper_1) > 0:
        count_result.extend('result')
        if nb_operation[0] not in [' 2√x', ' 3√x', ' L circle_r', ' S circle_r', ' V ball_r', ' 1/x']:
            oper_1 = float(''.join(nb_oper_1))
            oper_2 = float(''.join(nb_oper_2))
            func_oper = nb_operation[0]
            nb_oper_1.clear()
            nb_oper_2.clear()
            lbl_screen['text'] = str(operation_result(oper_1, func_oper, oper_2))

            if count_operations[0] <= 1:
                nb_oper_1.extend(str(lbl_screen['text']))
                nb_operation.clear()
                nb_operation.append(names_buttons[row][col])

            else:
                nb_oper_1.extend(lbl_screen['text'])

            nb_operation.clear()
            nb_operation.append(names_buttons[row][col])
            count_operations[0] = 0

        else:
            oper_1 = float(''.join(nb_oper_1))
            func_oper = nb_operation[0]
            nb_oper_1.clear()
            nb_oper_2.clear()
            lbl_screen['text'] = str(operation_result(oper_1, func_oper))
            nb_oper_1.extend(str(lbl_screen['text']))
            nb_operation.clear()
            nb_operation.append(names_buttons[row][col])


    elif len(nb_oper_1) > 0 and names_buttons[row][col] in operations:
        count_operations[0] += 1
        if count_operations[0] == 1:
            nb_operation.clear()
            nb_operation.append(names_buttons[row][col])
            lbl_screen['text'] += (names_buttons[row][col])

        elif count_operations[0] > 1:
            if len(nb_oper_2) == 0:
                nb_operation.clear()
                nb_operation.append(names_buttons[row][col])
                lbl_screen['text'] += (names_buttons[row][col])

            else:
                lbl_screen['text'] += (names_buttons[row][col])
                oper_1 = float(''.join(nb_oper_1))
                oper_2 = float(''.join(nb_oper_2))
                func_oper = nb_operation[0]
                nb_oper_1.clear()
                nb_oper_2.clear()
                nb_operation.clear()
                nb_operation.append(names_buttons[row][col])
                if func_oper == '/' and oper_2 == 0:
                    lbl_screen['text'] = 'error'
                    count_result.clear()
                    count_operations[0] = 0
                    nb_operation.clear()
                    nb_oper_1.clear()
                    nb_oper_2.clear()
                else:
                    nb_oper_1.extend(operation_result(oper_1, func_oper, oper_2))
                    oper_1 = float(''.join(nb_oper_1))



    elif names_buttons[row][col] == 'CE':
        count_result.clear()
        count_operations[0] = 0
        nb_operation.clear()
        nb_oper_1.clear()
        nb_oper_2.clear()
        lbl_screen['text'] = ''


for i in range(len(names_buttons)):
    for j in range(len(names_buttons[i])):
        btn_buttons = tk.Button(
            master=window,
            relief=tk.RIDGE,
            borderwidth=3,
            text=names_buttons[i][j],
            font=fontExample,
            bg="GREEN",
            command=lambda row=i, col=j: value_lbl_screen(row, col)
        )
        btn_buttons.grid(row=i, column=j, sticky="nsew")

window.mainloop()