import math
import os
import random
import re
import sys

def jumpingOnClouds(c, k):
    energy = 100
    n = len(c)
    pos = 0    
    while True:
        pos = (pos + k) % n
        energy -= 1 + 2 * c[pos]
        if pos == 0:
            break
            
    return energy
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
