#Problem Link: https://www.hackerrank.com/challenges/30-recursion/problem?isFullScreen=true

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(N):
    '''Function to calculate the factorial'''
    if N <= 1:
        return 1
    else:
        return N * factorial(N-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
