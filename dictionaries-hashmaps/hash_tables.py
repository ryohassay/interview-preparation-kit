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
    isIncluded = 'Yes'
    size = len(magazine)
    for i, word in enumerate(note):
        for j in range(size - i):
            if word == magazine[j]:
                del magazine[j]
                break
        else:
            isIncluded = 'No'  # if the inner loop ended normally = the word wasn't found
            break

    print(isIncluded)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
