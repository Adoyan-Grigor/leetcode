#!/usr/bin/python3

'''leetcode_4'''


def int_toroman(num: int) -> str:
    '''https://leetcode.com/problems/integer-to-roman/'''
    res = ''
    mapping = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
               50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    while num != 0:
        for key, value in mapping.items():
            if num >= key:
                dividend = int(num/key)
                num %= key
                res += dividend*value
    return res
