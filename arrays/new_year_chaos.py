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
    num_swaps = 0
    for i in range(len(q) - 1):
        orig_pos = q[i] - 1
        if orig_pos - i > 2:
            print('Too chaotic')
            return
        else:
            for j in range(i + 1, len(q)):
                if q[i] > q[j]:
                    num_swaps += 1
    print(num_swaps)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
