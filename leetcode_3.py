#!/usr/bin/python3
'''3'''


def two_sum(nums, target):
    '''https://leetcode.com/problems/two-sum/'''
    res = []
    llist = []
    for i in nums:
        llist.append(int(i))
    for index, value in enumerate(llist):
        check = llist[index:]
        for xindex, xvalue in enumerate(check, index):
            if value + xvalue == target and index != xindex:
                res.append(index)
                res.append(xindex)
                return res
    return res
