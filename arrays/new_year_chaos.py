#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    size = len(q)
    swaps = [0] * size
    num_swaps = 0
    for i in range(size):
        for j in range(size - i - 1):
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                swaps[q[j+1]-1] += 1
                num_swaps += 1

    if max(swaps) > 2:
        print('Too chaotic')
    else:
        print(num_swaps)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
