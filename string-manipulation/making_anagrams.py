#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    a_dict = {}
    b_dict= {}
    count = 0

    for char in a:
        if a_dict.get(char) is None:
            a_dict[char] = 1
        else:
            a_dict[char] += 1

    for char in b:
        if b_dict.get(char) is None:
            b_dict[char] = 1
        else:
            b_dict[char] += 1

    ascii_a = 97
    num_alphabet = 26
    for i in range(ascii_a, ascii_a + num_alphabet):
        if a_dict.get(chr(i)) is None:
            if b_dict.get(chr(i)) is not None:
                count += b_dict[chr(i)]
        else:
            if b_dict.get(chr(i)) is None:
                count += a_dict[chr(i)]
            else:
                count += abs(a_dict[chr(i)] - b_dict[chr(i)])

    return count







if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
