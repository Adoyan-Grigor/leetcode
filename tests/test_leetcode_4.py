'''https://leetcode.com/problems/integer-to-roman/
Roman numerals are represented by seven different
symbols: I, V, X, L, C, D and M.'''
import pytest

from leetcode.leetcode_4 import int_toroman


@pytest.mark.parametrize("num, result", [(3, "III"), (4, "IV"),
                         (9, "IX"), (58, "LVIII"), (1994, "MCMXCIV")])
def test_4(num, result):
    '''test_leetcode_4'''
    assert int_toroman(num) == result


@pytest.mark.parametrize("num, result", [(3, "IIV"), (4, "IIII"),
                         (9, "VIIII"), (58, "LIIX"), (1994, "MMXCIV")])
def test_4_negative(num, result):
    '''negative_test_leetcode_4'''
    assert int_toroman(num) != result
