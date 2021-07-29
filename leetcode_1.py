#!/usr/bin/python3

'''leetcode_1
   performs the task by reference
   (https://leetcode.com/problems/excel-sheet-column-number/)'''


def title_to_number(columntitle: str) -> int:
    '''Given the string column_title representing the column title,
       returns the corresponding column number.'''
    res = 0
    my_case = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7,
               "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
               "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
               "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    for i in columntitle:
        res *= 26
        res += my_case[i]
    return res
