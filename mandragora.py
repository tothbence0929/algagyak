#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'mandragora' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY H as parameter.
#

def mandragora(H):
    # Write your code here
    H.sort()
    s = 1
    
    max_experience = total_health = sum(H)
    
    for health in H:
        total_health -= health
        s += 1
        
        if s * total_health > max_experience:
            max_experience = s * total_health
        else:
            break
    
    return max_experience

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        H = list(map(int, input().rstrip().split()))

        result = mandragora(H)

        fptr.write(str(result) + '\n')

    fptr.close()
