import math
import os
import random
import re
import sys

def plusMinus(arr):
    num = len(arr)
    nagative = []
    positive = []
    zero = []
    for i in arr:
        if i < 0:
            nagative.append(i)
        elif i > 0:
            positive.append(i)
        else:
            zero.append(i)
            
    print(f'{(len(positive)/num):.6f}')
    print(f'{(len(nagative)/num):.6f}')
    print(f'{(len(zero)/num):.6f}')

    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
