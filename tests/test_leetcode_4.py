'''tests the int_torman function in leetcode_4.py file
   converts integer num to roman numbers'''

import pytest

from ..leetcode_4 import int_toroman


@pytest.mark.parametrize("num, result", [(3, "III"), (4, "IV"),
                         (9, "IX"), (58, "LVIII"), (1994, "MCMXCIV")])
def test_4(num: int, result: str):
    '''test_leetcode_4'''
    assert int_toroman(num) == result


@pytest.mark.parametrize("num, result", [(3, "IIV"), (4, "IIII"),
                         (9, "VIIII"), (58, "LIIX"), (1994, "MMXCIV")])
def test_4_negative(num: int, result: str):
    '''negative_test_leetcode_4'''
    assert int_toroman(num) != result
