'''tests the is_anagram function in leetcode_2.py file
   Given two strings st_s and st_t, returns true if st_t is
   an anagram of st_s, and false otherwise.'''

import pytest

from leetcode.leetcode_2 import is_anagram


@pytest.mark.parametrize("st_s, st_t, result", [('anagram', 'nagaram', 'True'),
                         ('rat', 'car', 'False'), ('a', 'a', 'True'), ('a', 'b', 'False')])
def test_2(st_s: str, st_t: str, result: str):
    '''test_leetcode_2'''
    assert is_anagram(st_s, st_t) == result


@pytest.mark.parametrize('st_s, st_t, result', [('aasd', 'asd', 'True'),
                         ('bca', 'abc', 'False')])
def test_2_negative(st_s: str, st_t: str, result: str):
    '''negative_test_leetcode_2'''
    assert is_anagram(st_s, st_t) != result
