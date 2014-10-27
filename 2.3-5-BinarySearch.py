#!/usr/bin/env python
# 2.1 - Insertion Sort
# p.18
import time
import random

import BCLogging as log
    
    
# Start here 
A = [5, 2, 4, 6, 1, 3]
#A = [31, 41, 59, 26, 41, 58]
#log.logStart()
#A = [random.randint(1,100) for x in range(10000)]
#log.logEnd()

def binarySearch(A,toFind):
    if len(A) == 1:
        if toFind == A[0]:
            print True
        else:
            print False
    else:
        mid = int(len(A)/2)
        if toFind < A[mid]:
            binarySearch(A[:mid],toFind)
        else:
            binarySearch(A[mid:],toFind)
        



print("-"*25)  
print("Increasing")
print("In: {}".format(A))
log.logStart()
binarySearch(sorted(A),12)
log.logEnd()
print("-"*25)























