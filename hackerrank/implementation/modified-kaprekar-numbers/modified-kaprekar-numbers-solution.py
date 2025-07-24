import math
import os
import random
import re
import sys

def kaprekarNumbers(p, q):
    found = False
    for i in range(p, q + 1):
        d = len(str(i))
        sq = str(i * i)
        r = sq[-d:]
        l = sq[:-d] if len(sq) > d else '0'
        if int(l) + int(r) == i:
            print(i, end=' ')
            found = True
    if not found:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
