#!/usr/bin/python3
'''leetcode_3
   performs the task by reference
   https://leetcode.com/problems/two-sum/'''


def two_sum(nums: list, target: int) -> list:
    '''Given an array of integers nums and an integer target, returns the
       indices of two numbers so that they add up to the target value.'''
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
