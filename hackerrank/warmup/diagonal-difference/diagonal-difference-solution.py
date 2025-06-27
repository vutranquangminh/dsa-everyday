import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    # Write your code here
    ltor = 0
    rtol = 0
    size = len(arr)
    for i in range(len(arr)):
        ltor += arr[i][i]
        rtol += arr[i][size-i-1]
        
    return abs(ltor - rtol)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
