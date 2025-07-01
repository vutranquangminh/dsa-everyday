import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    birds = {}
    for bird in arr:
        if bird in birds:
            birds[bird] += 1
        else:
            birds[bird] = 1
     
    res = []
    for bird in birds: 
        if birds[bird] == max(birds.values()):
            res.append(bird)
            
    return min(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()