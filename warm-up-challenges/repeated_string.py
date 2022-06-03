#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    len_str = len(s)
    num_occur = int(n / len_str)
    num_remainder = n % len_str

    num_chars_substr = s.count('a')
    num_chars_remainder = s[:num_remainder].count('a')
    num_chars = num_chars_substr * num_occur + num_chars_remainder
    return num_chars



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
