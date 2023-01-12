###############################################################################
# FILE: largest_and_smallest.py
# WRITER:Daniel
# EXCERCISE: intro2cs2 ex2 
# a function that finds the max and min of three given numbers
# the first exceptional case shows what happens when all numbers are equal thus
# the maximal and minimal result should be the same number
# the second exceptional case will have negative numbers, to see that
# no problem occurs when changing signs
###############################################################################

def max_of_three(num1,num2,num3):
    num_list = [num1, num2, num3]
    result = num1
    for i in num_list:
        if result < i:
            result = i
    return result

def min_of_three(num1,num2,num3):
    num_list = [num1, num2, num3]
    result = num1
    for i in num_list:
        if result > i:
            result = i
    return result

def largest_and_smallest(num1,num2,num3):
    max_num = max_of_three(num1, num2, num3)
    min_num = min_of_three(num1, num2, num3)
    return max_num, min_num

def check_largest_and_smallest():
    """a testing function"""
    test1 = (largest_and_smallest(17,1,6) == (17, 1))
    test2 = (largest_and_smallest(1,17,6) == (17, 1))
    test3 = (largest_and_smallest(1, 1, 2) == (2, 1))
    test4 = (largest_and_smallest(0, 0, 0) == (0, 0))
    test5 = (largest_and_smallest(-1, -17, -6) == (-1, -17))

    return (test1 == test2 == test3 == test4 == test5 == True)
