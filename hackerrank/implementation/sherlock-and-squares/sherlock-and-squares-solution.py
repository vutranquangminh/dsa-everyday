import math
import os
import random
import re
import sys

def squares(a, b):
    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))
    return max(0, end - start + 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
