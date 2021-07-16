#!/usr/bin/python3

'''leetcode_3'''


def two_sum(nums: list, target: int) -> list:
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
