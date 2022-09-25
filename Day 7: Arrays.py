#Problem Link : https://www.hackerrank.com/challenges/30-arrays/problem?isFullScreen=true

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    b = list(map(int, input().split(" ")))

    for i in range(1, n+1):
        print(b[n-i], end=" ")
