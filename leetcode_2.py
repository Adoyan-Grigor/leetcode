#!/usr/bin/python3
'''leetcode_2
   performs the task by reference
   (https://leetcode.com/problems/valid-anagram/)'''


def is_anagram(st_s: str, st_t: str) -> bool:
    '''Given two strings st_s and st_t, returns true if st_t is
       an anagram of st_s, and false otherwise.'''
    if len(st_s) != len(st_t):
        res = False
        return res
    for i in st_s:
        s_num = 0
        t_num = 0
        for index_s in st_s:
            if index_s == i:
                s_num += 1
        for index_t in st_t:
            if index_t == i:
                t_num += 1
        if s_num != t_num:
            res = False
            return res
    res = True
    return res
