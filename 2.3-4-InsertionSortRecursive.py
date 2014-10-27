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

# Takes 8s to sort range(10000)
# Runs in 3s on Ubuntu. Python2x

def insertionSort(A):
    #print("In: " + str(A))

    for j in range(1,len(A)):
        key = A[j]
        # Insert A[j] into sorted array A[0..j-1]
        i = j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
        #print("Mid:" + str(A))
    
    #print("Out:" + str(A))
    
def insert(A,p):
    L = A[:p]
    R = A[p:]
    
    print("L: {}".format(L))
    print("R: {}".format(R))
    
    


def insertionSortRecursive(A,p):
    # Want to sort A[0..n] by first sorting A[0..n-1] recursively
    # and then inserting A[n] into the sorted array A[0..n-1]
    
    if p > 1:
        p -= 1
        insertionSortRecursive(A,p)
        insert(A,p)




  
  

print("-"*25)  
print("Increasing")
print("In: {}".format(A))
log.logStart()
insertionSortRecursive(A,len(A))
log.logEnd()
print("-"*25)























