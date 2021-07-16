'''https://leetcode.com/problems/find-all-anagrams-in-a-string/
Given two strings s and p, return an array of all the start
indices of p's anagrams in s.
You may return the answer in any order.'''

import pytest

from leetcode.leetcode_9 import find_anagrams


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
