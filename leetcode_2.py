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
    list_t = []
    for i in st_t:
        list_t.append(i)
    for i in st_s:
        if i in list_t:
            list_t.remove(i)
        else:
            res = False
            return res
    res = True
    return res
