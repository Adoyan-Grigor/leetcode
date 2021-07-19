'''https://leetcode.com/problems/median-of-two-sorted-arrays/
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).'''
import pytest

from leetcode.leetcode_7 import find_median_sorted_arrays


@pytest.mark.parametrize('num1, num2, result', [('1 3', '2', 2), ('1 2', '3 3',
                         2.5), ('0 0', '0 0', 0), ('', '1', 1), ('2', '', 2)])
def test_7(num1: str, num2: str, result):
    '''test_leetcode_7'''
    assert find_median_sorted_arrays(num1.split(), num2.split()) == result


@pytest.mark.parametrize('num1, num2, result', [('1 3', '2', 3), ('1 2', '3 3',
                         2), ('', '1', ''), ('2', '', '')])
def test_7_negative(num1: str, num2: str, result):
    '''negative_test_leetcode_7'''
    assert find_median_sorted_arrays(num1.split(), num2.split()) != result
