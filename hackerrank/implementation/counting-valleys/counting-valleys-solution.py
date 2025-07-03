import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    elevation = 0
    valleys = 0
    for step in path:
        if step == 'U':
            elevation += 1
            if elevation == 0:
                valleys += 1
        else:
            elevation -= 1

    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()