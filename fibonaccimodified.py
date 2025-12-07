#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

def fibonacciModified(t1, t2, n):
    dp = [0] * n
    
    dp[0] = t1
    dp[1] = t2

    for i in range(2, n):
        dp[i] = dp[i-2] + dp[i-1] * dp[i-1]

    return dp[n - 1]

if __name__ == '__main__':
    
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
     
        fptr = sys.stdout

   
    try:
        first_multiple_input = sys.stdin.readline().rstrip().split()
    except EOFError:
        first_multiple_input = []
    
    if len(first_multiple_input) >= 3:
        t1 = int(first_multiple_input[0])
        t2 = int(first_multiple_input[1])
        n = int(first_multiple_input[2])
    else:
        
        t1, t2, n = 0, 0, 0
        if fptr != sys.stdout:
            fptr.close()
        sys.exit(0)

  
    result = fibonacciModified(t1, t2, n)

    
    fptr.write(str(result) + '\n')

   
    if fptr != sys.stdout:
        fptr.close()
