#!/usr/bin/python3
'''leetcode_5'''


def roman_to_int(st_s):
    '''https://leetcode.com/problems/roman-to-integer/'''
    the_w = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    st_s += "|"
    for index, value in enumerate(st_s):
        check = st_s[index + 1]
        if check == '|':
            res += the_w[value]
            break
        if the_w[value] < the_w[check]:
            res -= the_w[value]
        elif the_w[value] >= the_w[check]:
            res += the_w[value]
    return res
