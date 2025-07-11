import math
import os
import random
import re
import sys

def appendAndDelete(s, t, k):
    diff = 0
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            break
        diff += 1
    steps = len(s) + len(t) - 2 * diff
    if steps > k:
        return "No"
    if (k - steps) % 2 == 0 or k >= len(s) + len(t):
        return "Yes"
    return "No"

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
