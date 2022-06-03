#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    max_sum = -64  # Possible range of sum [-63, 63]
    arr_size, hourglass_size, midpoint = 6, 3, 1

    for i in range(arr_size - hourglass_size + 1):
        for j in range(arr_size - hourglass_size + 1):
            sigma = sum(arr[i][j: j + hourglass_size]) + arr[i + midpoint][j + midpoint] + sum(arr[i + 2][j: j + hourglass_size])
            if sigma > max_sum:
                max_sum = sigma
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
