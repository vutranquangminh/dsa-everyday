import math
import os
import random
import re
import sys

def birthday(s, d, m):
    res = 0
    for i in range(len(s) - m + 1):
        store = 0
        for j in range(m):
            store += s[i + j]
        if store == d:
            res += 1
    return res

            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()