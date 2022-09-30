#Problem Link: https://www.hackerrank.com/challenges/30-binary-numbers/problem?isFullScreen=true

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    rmd = []
    
    while n > 0:
        rm = n % 2
        n = n//2
        rmd.append(rm)
    
    count,result = 0,0
    
    for i in range(0,len(rmd)):
        if rmd[i] == 0:
            count = 0
        else:
            count +=1
            result = max(result,count)
    
    print(result)
