import math
import os
import random
import re
import sys

def viralAdvertising(n):
    shared = 5
    cumulative_likes = 0

    for day in range(1, n + 1):
        liked = shared // 2
        cumulative_likes += liked
        shared = liked * 3

    return cumulative_likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
