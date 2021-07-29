'''tests the partition_labels function in leetcode_8.py file
   splits the string into as many parts as possible so that
   each letter appears in at most one part.'''

import pytest

from leetcode.leetcode_8 import partition_labels


@pytest.mark.parametrize("st_s, result", [('ababcbacadefegdehijhklij',
                         [9, 7, 8]), ('eccbbbbdec', [10])])
def test_8(st_s: str, result):
    '''test_leetcode_8'''
    assert partition_labels(st_s) == result


@pytest.mark.parametrize("st_s, result", [('ababcbacadefegdehijhklij',
                         [0, 7, 8]), ('eccbbbbdec', [0])])
def test_8_negative(st_s: str, result):
    '''negative_test_leetcode'''
    assert partition_labels(st_s) != result
