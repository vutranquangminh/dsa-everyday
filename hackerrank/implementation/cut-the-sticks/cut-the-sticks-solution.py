import math
import os
import random
import re
import sys

def cutTheSticks(arr):
    res = []
    while len(arr) > 0:
        res.append(len(arr))
        min_stick = min(arr)
        arr = [stick - min_stick for stick in arr if stick - min_stick > 0]
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
