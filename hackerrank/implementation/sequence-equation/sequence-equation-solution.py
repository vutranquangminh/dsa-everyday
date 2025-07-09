import math
import os
import random
import re
import sys

def permutationEquation(p):
    res = []
    for x in range(1, len(p) + 1):
        i = p.index(x) + 1
        j = p.index(i) + 1
        res.append(j)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
