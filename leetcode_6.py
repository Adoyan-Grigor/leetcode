#!/usr/bin/python3
'''leetcode_6'''


def longest_palindrome(st_s):
    '''https://leetcode.com/problems/longest-palindromic-substring/'''
    if not st_s or len(st_s) == 1:
        return st_s
    min_start, max_len = 0, 1
    i = 0
    while i < len(st_s):
        if len(st_s) - i <= max_len / 2:
            break
        j, k = i, i
        while k < len(st_s) - 1 and st_s[k + 1] == st_s[k]:
            k += 1
        i = k + 1
        while k < len(st_s) - 1 and j > 0 and st_s[k + 1] == st_s[j - 1]:
            k += 1
            j -= 1
        new_len = k - j + 1
        if new_len > max_len:
            min_start = j
            max_len = new_len
    res = st_s[min_start:min_start+max_len]
    return res
