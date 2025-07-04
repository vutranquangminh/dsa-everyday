import math
import os
import random
import re
import sys

def pickingNumbers(a):
    from collections import Counter
    freq = Counter(a)
    max_len = 0
    for num in freq:
        current = freq[num]
        next_num = freq.get(num + 1, 0)
        max_len = max(max_len, current + next_num)
    return max_len


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
