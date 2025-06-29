import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # Write your code here
    arr = []
    for i in grades:
        if i > 37:
            m = i%5
            if  m > 2:
                n = 5 - m
                i = i + n
        arr.append(i)       
    
    return arr 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()