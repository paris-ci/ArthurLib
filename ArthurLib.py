#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""ArthurLib -- ArthurLib.py
Add a number of useful functions to python, for scripting
"""

# ------------------------------------------------------------------------------
__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — Do What The Fuck You Want To Public Licence"

# --  IMPORTS  -----------------------------------------------------------------

# --   CONST   -----------------------------------------------------------------

# Unix terminal colors

normal = "\033[0m"
bold = "\033[1m"
underline = "\033[4m"
blink = "\033[5m"
reverse = "\033[7m"
concealed = "\033[8m"

black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white ="\033[37m"

on_black = "\033[40m"
on_red = "\033[41m"
on_green = "\033[42m"
on_yellow = "\033[43m"
on_blue = "\033[44m"
on_magenta = "\033[45m"
on_cyan = "\033[46m"
on_white = "\033[47m"

# -- FUNCTIONS -----------------------------------------------------------------
## --  INPUTS   ----------------------------------------------------------------

def check_is_int(number):
    """Check if the argument is an integer

    :param number: int — The int to test"""
    try:
        if type(number) is bool:
            return False
        number = int(number)
        return True
    except TypeError:
        return False
    except ValueError:
        return False


def check_is_float(number):
    """Check if the argument is a floating point number

    :param number: float — The float to test
    """
    try:
        if type(number) is bool:
            return False
        number = float(number)
        return True
    except TypeError:
        return False
    except ValueError:
        return False


def float_is_between(number, min=None, max=None):
    """Check if a float or a number is between a minimum value and a maximum value.

    :param number: float — Number to test
    :param min: float — Minimal value
    :param max: float — Maximal value
    :return: 0 (ok), 1 (too big), 2 (too small)
    """

    if min is None and max is None:
        return 0 # OK
    elif min is not None and max is None:
        if number >= min:
            return 0 # OK
        else:
            return 2 # Too small
    elif min is None and max is not None:
        if number <= max:
            return 0 # OK
        else:
            return 1 # Too big
    else:
        if number >= min:
            if number <= max:
                return 0 # OK
            else:
                return 1 # Too big
        else:
            return 2 # Too small

def safe_input_int(min=None, max=None, inputMessage="Enter a number >", messageNotInt="Please enter a valid number.", messageTooSmall="This number is too small.", messageTooBig="This number is too big."):
    """Ask a user to input an integer.

    :param min: int — The minimal value of the integer
    :param max: int — The maximal value of the integer
    :param inputMessage: str — The massage to ask for the integer
    :param messageNotInt: str — The message to show if the input in not an integer
    :param messageTooSmall: str — The message to show if the input is too small
    :param messageTooBig: str — The message to show if the input is too big
    :return: int — The input number
    """
    while True:
        number = input(inputMessage)
        if check_is_int(number):
            number = int(number)
            inter = float_is_between(number, min, max)
            if inter == 0:
                return number
            elif inter == 1:
                print(messageTooBig)
            else:
                print(messageTooSmall)
        else:
            print(messageNotInt)

def safe_input_float(min=None, max=None, inputMessage="Enter a number >", messageNotInt="Please enter a valid number.", messageTooSmall="This number is too small.", messageTooBig="This number is too big."):
    """Ask a user to input an float.

    :param min: float — The minimal value of the float
    :param max: float — The maximal value of the float
    :param inputMessage: str — The massage to ask for the float
    :param messageNotInt: str — The message to show if the input in not an float
    :param messageTooSmall: str — The message to show if the input is too small
    :param messageTooBig: str — The message to show if the input is too big
    :return: float — The input number
    """
    while True:
        number = input(inputMessage)
        if check_is_int(number):
            number = float(number)
            inter = float_is_between(number, min, max)
            if inter == 0:
                return number
            elif inter == 1:
                print(messageTooBig)
            else:
                print(messageTooSmall)
        else:
            print(messageNotInt)


## --   FILES   ----------------------------------------------------------------


def getLastLine(file):
    """Get the last line of a file.

    :param file: str — The file to open
    :return: str — the last line of the file
    """
    with open(file, "rb") as f:
        f.seek(-2, 2)            # Jump to the second last byte.
        while f.read(1) != "\n": # Until EOL is found...
            f.seek(-2, 1)        # ...jump back the read byte plus one more.
        last = str(f.readline()) # Read last line.

    return last

## --  OUTPUTS  ----------------------------------------------------------------

