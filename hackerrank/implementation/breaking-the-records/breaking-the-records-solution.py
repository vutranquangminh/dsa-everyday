import math
import os
import random
import re
import sys

def breakingRecords(scores):
    # Write your code here
    maxcount = 0
    maxscore = scores[0]
    mincount = 0
    minscore = scores[0]
    
    for i in range(1,len(scores)):
        if scores[i] > maxscore:
            maxcount += 1
            maxscore = scores[i]
        elif scores[i] < minscore:
            mincount += 1
            minscore = scores[i]
    
    return [maxcount,mincount]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()