'''test_leetcode_8'''
import pytest

from leetcode.leetcode_8 import partition_labels


@pytest.mark.parametrize("st_s, result", [('ababcbacadefegdehijhklij',
                         [9, 7, 8]), ('eccbbbbdec', [10])])
def test_8(st_s, result):
    '''https://leetcode.com/problems/partition-labels/
       You are given a string s. We want to partition the string into as many
       parts as possible so that each letter appears in at most one part.
       Return a list of integers representing the size of these parts.'''
    assert partition_labels(st_s) == result


@pytest.mark.parametrize("st_s, result", [('ababcbacadefegdehijhklij',
                         [0, 7, 8]), ('eccbbbbdec', [0])])
def test_8_negative(st_s, result):
    '''negative-test'''
    assert partition_labels(st_s) != result
