import math
import os
import random
import re
import sys

def timeConversion(s):
    hour = int(s[:2])
    minute = int(s[3:5])
    second = int(s[6:8])
    period = s[8:]
    if period == 'AM':
        if hour == 12:
            hour = 0
    elif period == 'PM':
        if hour != 12:
            hour += 12
    
    return f'{hour:02}:{minute:02}:{second:02}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
