#!/usr/bin/python3
'''leetcode_8
   performs the task by reference
   https://leetcode.com/problems/partition-labels/'''


def partition_labels(st_s: str):
    '''splits the string into as many parts as possible so
       that each letter appears in at most one part'''
    res = []
    st_x = 0
    st_y = 1
    if len(st_s) == 1:
        return 1
    if len(st_s) == 2 and st_s[0] != st_s[1]:
        return 1, 1
    if len(st_s) == 2 and st_s[0] == st_s[1]:
        return 2
    while st_y != len(st_s) + 1:
        element = st_s[st_x:st_y]
        xelement = st_s[st_y:]
        for index, value in enumerate(element):
            if value in xelement:
                st_y += 1
                break
            if index == len(element) - 1:
                if value not in xelement:
                    res.append(len(element))
                    st_y += 1
                    st_x = st_y - 1
    return res
