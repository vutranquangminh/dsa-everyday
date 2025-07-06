import math
import os
import random
import re
import sys

def angryProfessor(k, a):
    on_time = sum(1 for time in a if time <= 0)
    if on_time >= k:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Number of test cases

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])  # Total students
        k = int(first_multiple_input[1])  # Threshold

        a = list(map(int, input().rstrip().split()))  # Arrival times

        result = angryProfessor(k, a)
        fptr.write(result + '\n')

    fptr.close()
