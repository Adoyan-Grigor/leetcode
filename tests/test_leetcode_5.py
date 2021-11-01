'''tests the roman_to_int function in leetcode_5.py file
   converts roman numbers to integers'''

import pytest

from ..leetcode_5 import roman_to_int


@pytest.mark.parametrize("st_s, result", [("III", 3), ("IV", 4), ("IX", 9),
                         ("LVIII", 58), ("MCMXCIV", 1994)])
def test_5(st_s: str, result: int):
    '''test_leetcode_5'''
    assert roman_to_int(st_s) == result


@pytest.mark.parametrize("st_s, result", [("III", 2), ("IV", 6), ("IX", 11),
                         ("LVIII", 580), ("MCMXCIV", 100105015)])
def test_5_negative(st_s: str, result: int):
    '''neagtive_test_leetcode_5'''
    assert roman_to_int(st_s) != result
