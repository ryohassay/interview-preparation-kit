#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    dict = {}
    for word in magazine:
        if dict.get(word) is None:
            dict[word] = 1
        else:
            dict[word] += 1

    for word in note:
        if dict.get(word) is not None:
            if dict[word] != 0:
                dict[word] -= 1
            else:
                print('No')
                return
        else:
            print('No')
            return

    print('Yes')

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
