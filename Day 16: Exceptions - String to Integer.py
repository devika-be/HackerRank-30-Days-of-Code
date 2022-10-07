#Problem Link: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem?isFullScreen=true

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

 
S = input().strip()

try:
    print(int(S))
except ValueError:
    print("Bad String")
