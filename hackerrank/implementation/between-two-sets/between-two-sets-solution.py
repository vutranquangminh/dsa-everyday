import math
import os
import random
import re
import sys

def getTotalX(a, b):
    lcm_a = a[0]
    for num in a[1:]:
        lcm_a = math.lcm(lcm_a, num)

    gcd_b = b[0]
    for num in b[1:]:
        gcd_b = math.gcd(gcd_b, num)

    count = 0
    x = lcm_a
    while x <= gcd_b:
        if gcd_b % x == 0:
            count += 1
        x += lcm_a
    return count    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
