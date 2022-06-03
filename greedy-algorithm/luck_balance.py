#!/bin/python3

from itertools import count
import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    importants, unimportants = [], []
    total = 0
    for contest in contests:
        if contest[1] == 1:
            importants.append(contest[0])
        else:
            # unimportants.append(contest[0])
            total += contest[0]

    importants.sort(reverse=True)
    size = len(importants)
    num = min(size, k)
    for i in range(num):
        total += importants[i]
    for i in range(num, size):
        total -= importants[i]

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
