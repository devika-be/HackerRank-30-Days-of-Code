#Problem Link: https://www.hackerrank.com/challenges/30-2d-arrays/problem?isFullScreen=true

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    ARRAY = []
    ADD = []
    MAX_SUM = []

    for _ in range(6):
        ARRAY.append(list(map(int, input().rstrip().split())))

    for i in range(len(ARRAY)-2):
        for j in range(4):
            ADD.extend(ARRAY[i][j:j+3])
            ADD.append(ARRAY[i+1][j+1])
            ADD.extend(ARRAY[i+2][j:j+3])
            MAX_SUM.append(sum(ADD))
            ADD = []

    print(max(MAX_SUM))
