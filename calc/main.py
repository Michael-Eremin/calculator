"""Graphing calculator program. Rendering a calculator using Tkinter.
Request for calculations in two modes. In sequential mode,
 the calculation is performed in the one_action.py module.
When parsing the whole line in the expression.py module."""

import tkinter as tk
import tkinter.font as tkFont
from expression import value_lbl_screen_str, clear_text
from one_action import value_lbl_screen, activate_ce_button

# Class 'tkinter' instance.
window = tk.Tk()

# Window options.
window.title('CALCULATOR')
window.columnconfigure([0, 1, 2, 3], weight=1, minsize=130)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6,7], weight=1, minsize=60)

# Font options.
fontExample = tkFont.Font(family="Arial", size=18, weight="normal",
                          slant="roman")
# Screen options.
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

# Working mode:
#   throughout the line: mode[0] == 1;
#   successively: mode[0] == 0.
# Start value:
mode = [0]


def select_mode(row: int, col: int):
    """Sets the mode.With the 'STR' button.
    In accordance with the mode calls modules for calculation.
    Displays the received text on the screen."""
    act_btn = names_buttons[row][col]
    if act_btn == 'STR':
        if mode[0] == 1:
            lbl_screen['text'] = ''
            clear_text()
            mode[0] = 0
        else:
            lbl_screen['text'] = ''
            activate_ce_button()
            mode[0] = 1
        make_widget_str()
        make_widget_mode_str()
    if mode[0] == 1:
        text = value_lbl_screen_str(act_btn)
        lbl_screen['text'] = text
    else:
        text = value_lbl_screen(act_btn)
        lbl_screen['text'] = text

def btn_buttons(i: int, j: int, color_mode: str):
    """Assigns properties and values to buttons."""
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
    """Drawing common buttons for two modes."""
    for i in range(0,7):
        for j in range(len(names_buttons[i])):
            color_mode = "#01C624"
            btn_buttons(i, j, color_mode)


def make_widget_str():
    """Drawing the 'STR' button. Mode selection button.
    Changes color when selected."""
    for i in range(7, 8):
        for j in range(0,1):
            if mode[0] == 1:
                color_mode = "#FFF38F"
                btn_buttons(i, j, color_mode)
            else:
                color_mode = "#8FFFA2"
                btn_buttons(i, j, color_mode)


def make_widget_mode_str():
    """Button rendering specifically for the sequential mode
     of the 'expression.py' module. Mode selection button.
     Change color when this mode is selected."""
    for i in range(7, 8):
        for j in range(1, 4):
            if mode[0] == 1:
                color_mode = "#01C624"
                btn_buttons(i, j, color_mode)
            else:
                color_mode = "#8FFFA2"
                btn_buttons(i, j, color_mode)


def make_widget():
    """Start creating buttons."""
    make_widget_not_mode_str()
    make_widget_str()
    make_widget_mode_str()



if __name__ == '__main__':
    make_widget()
    window.mainloop()
