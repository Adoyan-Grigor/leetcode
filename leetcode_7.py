#!/usr/bin/python3
'''7'''


def find_median_sorted_arrays(num1, num2):
    '''https://leetcode.com/problems/median-of-two-sorted-arrays/'''
    nums1 = []
    nums2 = []
    for i in num1:
        nums1.append(int(i))
    for i in num2:
        nums2.append(int(i))
    output_list = []
    while(nums1 and nums2):
        if nums1[0] <= nums2[0]:
            output_list.append(nums1.pop(0))
        else:
            output_list.append(nums2.pop(0))
    while nums1:
        output_list.append(nums1.pop(0))
    while nums2:
        output_list.append(nums2.pop(0))
    mid = len(output_list) // 2
    if len(output_list) % 2 != 0:
        res = (output_list[mid])
        return res
    res = (float(output_list[mid] + output_list[mid - 1]) / 2)
    return res
