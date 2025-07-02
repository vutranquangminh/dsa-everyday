import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    count = {}
    for sock in ar:
        count[sock] = count.get(sock, 0) + 1
    return sum(v // 2 for v in count.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
