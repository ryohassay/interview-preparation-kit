#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    num_swaps = 0
    size = len(a)
    for i in range(size):
        for j in range(size - i - 1):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]
                num_swaps += 1

    print('Array is sorted in {} swaps.'.format(num_swaps))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[size-1]))


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
