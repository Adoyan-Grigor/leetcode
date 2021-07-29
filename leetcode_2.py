#!/usr/bin/python3
'''leetcode_2
   performs the task by reference
   (https://leetcode.com/problems/valid-anagram/)'''


def is_anagram(st_s: str, st_t: str) -> str:
    '''Given two strings st_s and st_t, returns true if st_t is
       an anagram of st_s, and false otherwise.'''
    st_g = 0
    st_f = []
    for st_k in st_t:
        st_f.append(st_k)
    for st_i in st_s:
        if st_i in st_f:
            st_g += 1
            st_f.remove(st_i)
        else:
            res = 'False'
            return res
    if st_g == len(st_s) and len(st_s) == len(st_t):
        res = 'True'
        return res
    res = 'False'
    return res
