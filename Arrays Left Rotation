import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    roud = d%len(a)
    arr = a[roud:]
    arr.extend(a[:roud])
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
