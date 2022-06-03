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

    for i in range(size):
        org_pos = q[i] - 1
        if(i < org_pos):
            swaps[org_pos] = org_pos - i
            sub_q = q[i:(org_pos + 1)]
            sub_q = sub_q[1:swaps[org_pos]+1] + sub_q[:1]
            q[i:(org_pos + 1)] = sub_q

    if max(swaps) > 2:
        print('Too chaotic')
    else:
        print(sum(swaps))


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
