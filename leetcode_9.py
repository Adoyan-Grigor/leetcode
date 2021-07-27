#!/usr/bin/python3
'''leetcode_9
   performs the task by reference
   https://leetcode.com/problems/find-all-anagrams-in-a-string/'''


def find_anagrams(st_s: str, st_p: str):
    '''returns an array of all the starting
       indices of the anagrams st_p in st_s'''
    res = []
    for st_i in range(len(st_s)):
        st_y = 0
        st_x = []
        for check in st_p:
            st_x.append(check)
        check = st_s[st_i:st_i + len(st_p)]
        for st_k in check:
            if st_k in st_x:
                st_x.remove(st_k)
                st_y += 1
            else:
                break
            if st_y == len(st_p):
                res.append(st_i)
    return res
