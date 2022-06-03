#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    count_dict = {}
    size = len(s)
    for i in range(size):
        for j in range(i + 1, size + 1):
            sub_str = s[i:j]
            sorted_sub_str = ''.join(sorted(sub_str))
            if count_dict.get(sorted_sub_str) is None:
                count_dict[sorted_sub_str] = 1
            else:
                count_dict[sorted_sub_str] += 1

    total = 0
    for count in count_dict.values():
        if count >= 2:
            combs = math.comb(count, 2)
            total += combs

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
