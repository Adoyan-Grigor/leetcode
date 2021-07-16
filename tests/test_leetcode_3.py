'''https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target,
return indices of the two numbers
such that they add up to target. You may assume
that each input would have exactly
one solution, and you may not use the same element twice.
You can return the answer in any order.'''

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
