#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    size = len(c)
    num_steps = 0
    i = 0
    while i < size - 2:
        if c[i+2] == 0:
            i += 2
        else:
            i += 1
        num_steps += 1

    if i == size - 2:
        # i += 1
        num_steps += 1

    return num_steps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
