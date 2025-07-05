import math
import os
import random
import re
import sys

def utopianTree(n):
    height = 1
    for cycle in range(1, n + 1):
        if cycle % 2 == 1:
            height *= 2
        else:
            height += 1
    return height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
