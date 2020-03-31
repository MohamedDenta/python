#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def minb(b):
    i = 1
    min = 0
    while i < len(b):
        if b[min] > b[i]:
            min = i
        i += 1
    return min

# 2 4 // 4 , 8 , 16
# 16 32 96


def maxa(a):
    i = 1
    max = 0
    while i < len(a):
        if a[max] < a[i]:
            max = i
        i += 1
    return max


def getTotalX(a, b):
    # Write your code here
    min_b = b[minb(b)]
    max_a = a[maxa(a)]
    lst1 = []
    lst2 = []
    x, n = max_a, min_b
    while max_a <= min_b:
        b = True
        for t in a:
            if max_a % t != 0:
                b = False
                break
        if b:
            lst1.append(max_a)
        max_a = max_a+x
    for v in lst1:
        flag = True
        for u in b:
            if u % v != 0:
                flag = False
                break
        if flag:
            lst2.append(v)
    return len(lst2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
