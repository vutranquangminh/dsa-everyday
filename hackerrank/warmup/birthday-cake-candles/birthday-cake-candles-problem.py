import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    # Write your code here
    tallest = 0
    for i in candles:
        if tallest < i:
            tallest = i
    count = 0
    for i in candles:
        if i == tallest:
            count += 1
    
    print(count)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
