import math
import os
import random
import re
import sys

def saveThePrisoner(n, m, s):
    remaining_candies = m % n
    last_prisoner = (remaining_candies + s - 1) % n or n
    return last_prisoner

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
