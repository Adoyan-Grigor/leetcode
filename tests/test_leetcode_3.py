'''tests the two_sum function in leetcode_3.py file
   Given an array of integers nums and an integer target, returns the
   indices of two numbers so that they add up to the target value.'''
import pytest

from leetcode.leetcode_3 import two_sum


@pytest.mark.parametrize("nums, target, result", [("2 7 11 15", 9, [0, 1]),
                         ('3 2 4', 6, [1, 2]), ('3 3', 6, [0, 1])])
def test_3(nums: str, target: int, result: list):
    '''test_leetcode_3'''
    assert two_sum(nums.split(), target) == result


@pytest.mark.parametrize("nums, target, result", [("8 5 9", 9, [0]),
                         ('3 2 4', 15, [1, 2]), ('3 3', 6, [0, 0])])
def test_3_negative(nums: str, target: int, result: list):
    '''negative_test_leetcode_3'''
    assert two_sum(nums.split(), target) != result
