'''test_leetcode_6'''
import pytest

from leetcode.leetcode_6 import longest_palindrome


@pytest.mark.parametrize("st_s, result", [("babad", 'bab'), ('cbbd', 'bb'),
                         ('a', 'a'), ('ac', 'a')])
def test_6(st_s, result):
    '''https://leetcode.com/problems/longest-palindromic-substring/
       Given a string s, return the longest palindromic substring in s.'''
    assert longest_palindrome(st_s) == result


@pytest.mark.parametrize("st_s, result", [("babad", 'ba'), ('cbbd', 'b'),
                         ('a', '|'), ('ac', 'ac')])
def test_6x(st_s, result):
    '''negative-test'''
    assert longest_palindrome(st_s) != result
