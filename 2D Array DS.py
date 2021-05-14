import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    i,j=0,0
    maxnum=-1*9*9-1
    for i in range(len(arr)):
        if i == len(arr)-2:break
        for j in range(len(arr[i])):
            if j == len(arr[i])-2:break
            a,b,c,d,e,f,g=arr[i][j],arr[i][j+1],arr[i][j+2],arr[i+1][j+1],arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2]
            maxnum = max(maxnum,a+b+c+d+e+f+g)
    return maxnum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
