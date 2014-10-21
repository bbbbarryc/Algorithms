#!/usr/bin/env python
# 2.1-4 - n-bit binary number

import time
import random

startTime = 0.0
endTime = 0.0

def logStart():
    global startTime
    startTime = time.time()
    
def logEnd():
    global startTime, endTime
    endTime = time.time()
    print (endTime - startTime)
    
# Start here
# A, B are n bit
# C is n+1 bit
A = [1, 1, 0, 1, 1] # 27 in binary
B = [0, 1, 0, 0, 1] # 9 in binary
C = [0]*(len(A)+1)

def add(A,B):
    for i in range(len(A)-1,-1,-1):
        res = A[i] + B[i] + C[i+1]
        C[i+1] = int(res % 2)
        C[i] = int(res / 2)
    #print(C)
    return C

    
logStart()
print(add(A,B))
logEnd()
print("-"*25)


