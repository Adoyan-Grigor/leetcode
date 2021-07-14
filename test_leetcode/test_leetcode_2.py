'''test_leetcode_2'''
import pytest

from leetcode.leetcode_2 import is_anagram


@pytest.mark.parametrize("st_s, st_t, result", [('anagram', 'nagaram', True),
                         ('rat', 'car', False)])
def test_2(st_s, st_t, result):
    '''https://leetcode.com/problems/valid-anagram/
      Given two strings s and t, return true if t is an
      anagram of s, and false otherwise.'''
    assert is_anagram(st_s, st_t) == result


@pytest.mark.parametrize('st_s, st_t, result', [('aasd', 'asd', True),
                         ('bca', 'abc', False)])
def test_2_negative(st_s, st_t, result):
    '''negative-test'''
    assert is_anagram(st_s, st_t) != result
