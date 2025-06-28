import math
import os
import random
import re
import sys

def staircase(n):
    # Write your code here
    for i in range(n):
        print(' '*(n-i-1), end='')
        print('#'*(i+1))

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
