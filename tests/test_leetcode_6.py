'''tests the longest_palindrome function in leetcode_6.py file
   returns the longest palindromic substring in st_s'''

import pytest

from ..leetcode_6 import longest_palindrome


@pytest.mark.parametrize("st_s, result", [("babad", 'bab'), ('cbbd', 'bb'),
                         ('a', 'a'), ('ac', 'a')])
def test_6(st_s: str, result: str):
    '''test_leetcode_6'''
    assert longest_palindrome(st_s) == result


@pytest.mark.parametrize("st_s, result", [("babad", 'ba'), ('cbbd', 'b'),
                         ('a', '|'), ('ac', 'ac')])
def test_6_negative(st_s: str, result: str):
    '''negative_test_leetcode_6'''
    assert longest_palindrome(st_s) != result
