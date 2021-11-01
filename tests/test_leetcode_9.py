'''tests the find_anagrams function in leetcode_9.py file
   returns an array of all the starting
   indices of the anagrams st_p in st_s'''

import pytest

from ..leetcode_9 import find_anagrams


@pytest.mark.parametrize("st_s, st_p, result", [('cbaebabacd', 'abc', [0, 6]),
                         ('abab', 'ab', [0, 1, 2])])
def test_9(st_s: str, st_p: str, result):
    '''test_leetcode_9'''
    assert find_anagrams(st_s, st_p) == result


@pytest.mark.parametrize("st_s, st_p, result", [('cbaebabacd', 'abc', [0, 1]),
                         ('abab', 'ab', [0, 2])])
def test_9_negative(st_s: str, st_p: str, result):
    '''negative_test_leetcode_9'''
    assert find_anagrams(st_s, st_p) != result
