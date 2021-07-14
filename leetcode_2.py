#!/usr/bin/python3
'''leetcode_2'''


def is_anagram(st_s, st_t):
    '''https://leetcode.com/problems/valid-anagram/'''
    st_g = 0
    st_f = []
    for st_k in st_t:
        st_f.append(st_k)
    for st_i in st_s:
        if st_i in st_f:
            st_g += 1
            st_f.remove(st_i)
        else:
            res = False
            return res
    if st_g == len(st_s) and len(st_s) == len(st_t):
        res = True
        return res
    res = False
    return res
