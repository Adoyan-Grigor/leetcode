'''https://leetcode.com/problems/excel-sheet-column-number/
Given a string columnTitle that represents the column
title as appear in an Excel sheet,
return its corresponding column number.'''

import pytest
from leetcode.leetcode_1 import title_to_number


@pytest.mark.parametrize("columntitle, result", [("A", 1), ('AB', 28),
                         ('ZY', 701), ('FXSHRXW', 2147483647)])
def test_1(columntitle: str, result: int):
    '''test_leetcode_1'''
    assert title_to_number(columntitle) == result


@pytest.mark.parametrize("columntitle, result", [("ZY", 50),
                         ("C", 2), ('A', 5)])
def test_1_negative(columntitle: str, result: int):
    '''negative_test_leetcode_1'''
    assert title_to_number(columntitle) != result
