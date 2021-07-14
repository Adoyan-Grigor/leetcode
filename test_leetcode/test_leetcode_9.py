'''test_leetcode_9'''
import pytest

from leetcode.leetcode_9 import find_anagrams


@pytest.mark.parametrize("st_s, st_p, result", [('cbaebabacd', 'abc', [0, 6]),
                         ('abab', 'ab', [0, 1, 2])])
def test_9(st_s, st_p, result):
    '''https://leetcode.com/problems/find-all-anagrams-in-a-string/
       Given two strings s and p, return an array of all the start
       indices of p's anagrams in s.
       You may return the answer in any order.'''
    assert find_anagrams(st_s, st_p) == result


@pytest.mark.parametrize("st_s, st_p, result", [('cbaebabacd', 'abc', [0, 1]),
                         ('abab', 'ab', [0, 2])])
def test_9x(st_s, st_p, result):
    '''negative-test'''
    assert find_anagrams(st_s, st_p) != result
