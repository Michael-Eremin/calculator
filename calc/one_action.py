"""Function module for calculating the value by by separate functions.
 One after another. """

from math import pi

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
operations = ['+', '^', ' 2√x', ' 3√x', '-', '/', '*', ' L circle_r',
              ' S circle_r', ' V ball_r', ' 1/x']
operations_for_two_operands = ['+', '^', '-', '/', '*']
operations_for_first_operand = [' 2√x', ' 3√x', ' L circle_r', ' S circle_r',
                                ' V ball_r', ' 1/x']
operations_for_mode_str = ['STR', '(', ')', '<<<']

# Sequence of values of activated buttons for the First operand
first_operand_digits = []

# Sequence of values of activated buttons for the Next operand
next_operand_digits = []

# Values of activated buttons for the operation
operation_value = ['']

# Counting the Operation queue in the expression displayed on the screen
count_operations = [0]

# List to create a line for calculation.
lbl_screen_list = []

# List to create a string to display.
text_for_screen = []


def make_screen_text(text_screen: list) -> str:
    """Converts a list to a string for display."""
    text = ''.join(text_screen)
    return text


def check_process_status() -> list[str]:
    """Specifies the current status code.
    return:
    '_' == no values, is the first operand make;
    'result' == the result of the previous operation;
    '_F_of' == there is a first operand and a function
    for one operand (for first)
    '_F_ot' == there is a first operand and a function
    for two operands (for two)
    '_F_ot_N' == there is a first operand and a function
    for two operands and next operand
    """
    status = list()
    status.append('')
    if count_operations[0] == 0:
        status[0] = '_'
    elif first_operand_digits and not next_operand_digits:
        if count_operations[0] == 1 and operation_value[0] == '=':
            status[0] = 'result'
        # First choice of operation for one first operand
        elif count_operations[0] == 1 \
                and operation_value[0] in operations_for_first_operand:
            status[0] = '_F_of'
        # Selecting the next operation that will run the first one
        elif count_operations[0] >= 2 \
                and operation_value[0] in operations_for_first_operand:
            status[0] = '_F_of'
        # Selecting the next operation that will run the first one
        elif count_operations[0] >= 2 \
                and operation_value[0] in operations_for_two_operands:
            status[0] = '_F_ot'
        # First choice of operation for two operands
        elif count_operations[0] == 1 \
                and operation_value[0] in operations_for_two_operands:
            status[0] = '_F_ot'
        # Possible replacements for the first operation
        elif count_operations[0] >= 2 \
                and operation_value[0] in operations_for_first_operand:
            status[0] = '_F_of'
        # Possible replacements for the first operation
        elif count_operations[0] >= 2 \
                and operation_value[0] in operations_for_two_operands:
            status[0] = '_F_ot'
    elif next_operand_digits:
        status[0] = '_F_ot_N'
    return status


def calculate_result(operand_1: str, function: str, operand_2=None) -> str:
    """Value calculation."""
    operand_1 = float(operand_1)
    if operand_2 != '':
        operand_2 = float(operand_2)
    if function == '/':
        result_operation = operand_1 / operand_2
    if function == '*':
        result_operation = operand_1 * operand_2
    elif function == '+':
        result_operation = operand_1 + operand_2
    elif function == '-':
        result_operation = operand_1 - operand_2
    elif function == '^':
        result_operation = operand_1 ** operand_2
    elif function == ' 2√x':
        result_operation = operand_1 ** float(1 / 2)
    elif function == ' 3√x':
        result_operation = operand_1 ** float(1 / 3)
    elif function == ' L circle_r':
        result_operation = float(2) * float(pi) * operand_1
    elif function == ' S circle_r':
        result_operation = float(pi) * (operand_1 ** float(2))
    elif function == ' V ball_r':
        result_operation = float(4/3) * float(pi) * (operand_1 ** float(3))
    elif function == ' 1/x':
        result_operation = float(1) / operand_1
    return str(round(result_operation, 4))


def write_first_operand(act_btn: str) -> str:
    """Creates the first operand."""
    if act_btn != '.' or act_btn == '.' and '.' not in first_operand_digits:
        first_operand_digits.extend(act_btn)
        text_for_screen.append(act_btn)
        return make_screen_text(text_for_screen)


def write_next_operand(act_btn: str) -> str:
    """Creates the next operand."""
    if act_btn != '.' or act_btn == '.' and '.' not in next_operand_digits:
        next_operand_digits.extend(act_btn)
        text_for_screen.append(act_btn)
        return make_screen_text(text_for_screen)


def write_operation(act_btn: str) -> str:
    """Fixes the selected operation."""
    if text_for_screen[-1] not in numbers:
        text_for_screen.pop()
    text_for_screen.append(act_btn)
    return make_screen_text(text_for_screen)


def reset_status():
    """Returns the calculator to the start state."""
    count_operations[0] = 0
    operation_value[0] = ''
    first_operand_digits.clear()
    next_operand_digits.clear()


def call_calculation() -> str:
    """
    Prepares and passes to 'calculate_result'
     for calculation: operand_1, function and operand_2.
     Returns a result.
    """
    operand_1 = ''.join(first_operand_digits)
    operand_2 = ''.join(next_operand_digits)
    function = operation_value[0]
    intermediate_result = list()
    intermediate_result.append('')
    if function == '/' and float(operand_2) == 0:
        reset_status()
        intermediate_result[0] = 'division by zero'
    elif function == ' 1/x' and float(operand_1) == 0:
        reset_status()
        intermediate_result[0] = 'division by zero'
    else:
        intermediate_result[0] \
            = calculate_result(operand_1, function, operand_2)
        reset_status()
        first_operand_digits.extend(str(intermediate_result[0]))
    return intermediate_result[0]


def activate_equally_button(act_btn: str) -> str:
    """Activation of the button with the value of '='."""
    status = check_process_status()
    result = list()
    result.append(0)
    if status[0] == '_F_of' or status[0] == '_F_ot_N':
        result[0] = call_calculation()
        text_for_screen.clear()
        text_for_screen.append(str(result[0]))
        make_screen_text(text_for_screen)
    count_operations[0] = + 1
    operation_value[0] = act_btn
    return str(result[0])


def activate_number_button(act_btn: str) -> str:
    """Activation of the button with the value of the digit."""
    status = check_process_status()
    if status[0] != 'result':
        if status[0] == '_' and not operation_value[0]:
            return write_first_operand(act_btn)
        elif status[0] == '_' and operation_value[0]:
            reset_status()
            return write_first_operand(act_btn)
        elif status[0] == '_F_ot' or status[0] == '_F_ot_N':
            return write_next_operand(act_btn)


def activate_operation_button(act_btn: str) -> str:
    """Button activation with function_operator value."""
    status = check_process_status()
    result = list()
    result.append(0)
    if first_operand_digits:
        if status[0] == '_F_of' or status[0] == '_F_ot_N':
            result[0] = call_calculation()
            text_for_screen.clear()
            text_for_screen.append(str(result[0]))
            text_for_screen.append(act_btn)
        else:
            write_operation(act_btn)
        count_operations[0] = + 1
        operation_value[0] = act_btn
        return make_screen_text(text_for_screen)


def activate_ce_button() -> str:
    """Activation of the button with the value of 'CE'."""
    reset_status()
    text_for_screen.clear()
    return make_screen_text(text_for_screen)


def value_lbl_screen(act_btn: str) -> str:
    """
    Gets activated button values and puts them to work.
    >>> value_lbl_screen('3')
    '3'
    >>> value_lbl_screen('+')
    '3+'
    >>> value_lbl_screen('5')
    '3+5'
    >>> value_lbl_screen(' 3√x')
    '8.0 3√x'
    >>> value_lbl_screen('=')
    '2.0'
    """
    # For 'number'.
    if act_btn in numbers:
        return activate_number_button(act_btn)
    # For '='.
    elif act_btn == '=' and len(first_operand_digits) > 0:
        return activate_equally_button(act_btn)
    # For 'function_operator'.
    elif act_btn in operations:
        return activate_operation_button(act_btn)
    # For 'CE'.
    elif act_btn == 'CE':
        return activate_ce_button()
