#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    idx_dict = {val: i for i, val in enumerate(arr)}
    count = 0
    for i, val in enumerate(arr):
        orig_val = i + 1
        if val != orig_val:
            arr[idx_dict[orig_val]], arr[i] = arr[i], arr[idx_dict[orig_val]]
            idx_dict[orig_val], idx_dict[val] = idx_dict[val], idx_dict[orig_val]
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
