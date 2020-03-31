#!/bin/python3

import math
import os
import random
import re
import sys
#3 4 21 36 10 28 35 5 24 42
#4 0
# Complete the breakingRecords function below.
def breakingRecords(scores):
    min,max = scores[0]
    ret=[0,0]
    for s in scores:
        if s<min:
            ret[0]+=1
            min=s
        elif s>max:
            ret[1]+=1
            max = s
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
