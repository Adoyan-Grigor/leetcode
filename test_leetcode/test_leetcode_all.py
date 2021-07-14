'''test_leetcode_all'''
import pytest

from leetcode.leetcode_1 import title_to_number
from leetcode.leetcode_2 import is_anagram
from leetcode.leetcode_3 import two_sum
from leetcode.leetcode_4 import int_toroman
from leetcode.leetcode_5 import roman_to_int
from leetcode.leetcode_6 import longest_palindrome
from leetcode.leetcode_7 import find_median_sorted_arrays
from leetcode.leetcode_8 import partition_labels
from leetcode.leetcode_9 import find_anagrams


@pytest.mark.parametrize("columntitle, result", [("A", 1), ('AB', 28),
                         ('ZY', 701), ('FXSHRXW', 2147483647)])
def test_1(columntitle, result):
    '''test_leetcode_1'''
    assert title_to_number(columntitle) == result


@pytest.mark.parametrize("columntitle, result", [("ZY", 50),
                         ("C", 2), ('A', 5)])
def test_1x(columntitle, result):
    '''test_leetcode_1x'''
    assert title_to_number(columntitle) != result


@pytest.mark.parametrize("st_s, st_t, result", [('anagram', 'nagaram', True),
                         ('rat', 'car', False)])
def test_2(st_s, st_t, result):
    '''test_leetcode_2'''
    assert is_anagram(st_s, st_t) == result


@pytest.mark.parametrize('st_s, st_t, result', [('aasd', 'asd', True),
                         ('bca', 'abc', False)])
def test_2x(st_s, st_t, result):
    '''test_leetcode_2x'''
    assert is_anagram(st_s, st_t) != result


@pytest.mark.parametrize("nums, target, result", [("2 7 11 15", 9, [0, 1]),
                         ('3 2 4', 6, [1, 2]), ('3 3', 6, [0, 1])])
def test_3(nums, target, result):
    '''test_leetcode_3'''
    assert two_sum(nums.split(), target) == result


@pytest.mark.parametrize("nums, target, result", [("8 5 9", 9, [0]),
                         ('3 2 4', 15, [1, 2]), ('3 3', 6, [0, 0])])
def test_3x(nums, target, result):
    '''test_leetcode_3x'''
    assert two_sum(nums.split(), target) != result


@pytest.mark.parametrize("num, result", [(3, "III"), (4, "IV"),
                         (9, "IX"), (58, "LVIII"), (1994, "MCMXCIV")])
def test_4(num, result):
    '''test_leetcode_4'''
    assert int_toroman(num) == result


@pytest.mark.parametrize("num, result", [(3, "IIV"), (4, "IIII"),
                         (9, "VIIII"), (58, "LIIX"), (1994, "MMXCIV")])
def test_4x(num, result):
    '''test_leetcode_4x'''
    assert int_toroman(num) != result


@pytest.mark.parametrize("st_s, result", [("III", 3), ("IV", 4), ("IX", 9),
                         ("LVIII", 58), ("MCMXCIV", 1994)])
def test_5(st_s, result):
    '''test_leetcode_5'''
    assert roman_to_int(st_s) == result


@pytest.mark.parametrize("st_s, result", [("III", 2), ("IV", 6), ("IX", 11),
                         ("LVIII", 580), ("MCMXCIV", 100105015)])
def test_5x(st_s, result):
    '''test_leetcode_5x'''
    assert roman_to_int(st_s) != result


@pytest.mark.parametrize("st_s, result", [("babad", 'bab'), ('cbbd', 'bb'),
                         ('a', 'a'), ('ac', 'a')])
def test_6(st_s, result):
    '''test_leetcode_6'''
    assert longest_palindrome(st_s) == result


@pytest.mark.parametrize("st_s, result", [("babad", 'ba'), ('cbbd', 'b'),
                         ('a', '|'), ('ac', 'ac')])
def test_6x(st_s, result):
    '''test_leetcode_6x'''
    assert longest_palindrome(st_s) != result


@pytest.mark.parametrize('num1, num2, result', [('1 3', '2', 2), ('1 2', '3 3',
                         2.5), ('0 0', '0 0', 0), ('', '1', 1), ('2', '', 2)])
def test_7(num1, num2, result):
    '''test_leetcode_7'''
    assert find_median_sorted_arrays(num1.split(), num2.split()) == result


@pytest.mark.parametrize('num1, num2, result', [('1 3', '2', 3), ('1 2', '3 3',
                         2), ('', '1', ''), ('2', '', '')])
def test_7x(num1, num2, result):
    '''test_leetcode_7x'''
    assert find_median_sorted_arrays(num1.split(), num2.split()) != result


@pytest.mark.parametrize("st_s, result", [('ababcbacadefegdehijhklij',
                         [9, 7, 8]), ('eccbbbbdec', [10])])
def test_8(st_s, result):
    '''test_leetcode_8'''
    assert partition_labels(st_s) == result


@pytest.mark.parametrize("st_s, result", [('ababcbacadefegdehijhklij',
                         [0, 7, 8]), ('eccbbbbdec', [0])])
def test_8x(st_s, result):
    '''test_leetcode_8x'''
    assert partition_labels(st_s) != result


@pytest.mark.parametrize("st_s, st_p, result", [('cbaebabacd', 'abc', [0, 6]),
                         ('abab', 'ab', [0, 1, 2])])
def test_9(st_s, st_p, result):
    '''test_leetcode_9'''
    assert find_anagrams(st_s, st_p) == result


@pytest.mark.parametrize("st_s, st_p, result", [('cbaebabacd', 'abc', [0, 1]),
                         ('abab', 'ab', [0, 2])])
def test_9x(st_s, st_p, result):
    '''test_leetcode_9x'''
    assert find_anagrams(st_s, st_p) != result
