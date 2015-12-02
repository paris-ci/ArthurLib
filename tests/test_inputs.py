#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
ArthurLib -- test_inputs.py
Test for arthurlib.py
"""

# ------------------------------------------------------------------------------
__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — Do What The Fuck You Want To Public Licence"

# --  IMPORTS  -----------------------------------------------------------------

# import pytest
from ArthurLib import *


# --   FUNCT   -----------------------------------------------------------------
def test_is_doc():
    assert __doc__ is not None


def test_check_is_int_whint():
    numberlist = [-2, -1, 0, 0.1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 999, 9999, 99999, 123456789, "0", "1", "2", "10",
                  "100"]

    for number in numberlist:
        assert check_is_int(number) == True


def test_check_is_int_woint():
    notanumberlist = [True, False, "3ad", "a", "BLAH", hex(0), [0, 1], "thisisavery\nlong\tstring"]

    for notanumber in notanumberlist:
        assert check_is_int(notanumber) == False


def test_check_is_float_whfloat():
    numberlist = [-2, -1, 0, 0.1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 999, 9999, 99999, 123456789, "0", "1", "2", "10",
                  "100", "0.1"]

    for number in numberlist:
        assert check_is_float(number) == True


def test_check_is_float_wofloat():
    notanumberlist = [True, False, "3ad", "a", "BLAH", hex(0), [0, 1], "thisisavery\nlong\tstring"]

    for notanumber in notanumberlist:
        assert check_is_float(notanumber) == False


def test_float_is_between_ok():
    assert float_is_between(0) == 0
    assert float_is_between(174) == 0
    assert float_is_between(174, 173) == 0
    assert float_is_between(174, None, 175) == 0
    assert float_is_between(0, 0, 0) == 0
    assert float_is_between(5, 0, 10) == 0
    assert float_is_between(70, 60, 100) == 0
    assert float_is_between(6, 5, 7) == 0


def test_float_is_between_big():
    assert float_is_between(1, 0, 0) == 1
    assert float_is_between(174, None, 173) == 1
    assert float_is_between(11, 0, 10) == 1
    assert float_is_between(11110, 60, 100) == 1
    assert float_is_between(6, -7, 5) == 1


def test_float_is_between_small():
    assert float_is_between(-1, 0, 0) == 2
    assert float_is_between(174, 175) == 2
    assert float_is_between(-10, 0, 10) == 2
    assert float_is_between(70, 100, 1000) == 2
    assert float_is_between(2, 5, 7) == 2

# --   MAIN    -----------------------------------------------------------------
