import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    sum = 0
    for i in arr:
        sum += i
    
    min = sum - arr[-1]
    max = sum - arr[0]
    print(min, end=' ')
    print(max)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
