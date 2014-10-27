#!/usr/bin/env python

import BCLogging as log
import random

# Use "infinity" as our sentinel
# Very important to use "infinity" and not "None"
# Infinity is a number... well, sort of.  It works with gt and lt comparisons.
inf = float("inf")

A = [3, 41, 52, 26, 38, 57, 9, 49]
A = [2, 5, 4, 7, 1, 3, 8, 6]

A = [6,5,4,3,9,8,7,1]

A = [random.randint(1,100) for x in range(10000000)]
# Ubuntu:
# 100,000 = 0.7s
# 1,000,000 = 8s
# 10,000,000 = 8.9s

def merge(A,p,q,r):
    #print("Called with {}, {}, {}".format(p,q,r))
    n1 = q - p + 1
    n2 = r - q
    #print("n1: {}".format(n1))
    #print("n2: {}".format(n2))
    L = [inf]*(n1+1)
    R = [inf]*(n2+1)
    # Copy the appropriate sequences into L and R
    # A is split now into L[:mid] and R[mid:]
    for i in range(n1):
        #L.append(A[p + i])
        L[i] = A[p + i]
    for j in range(n2):
        #R.append(A[q + 1 + j])
        R[j] = A[q + j + 1]
    #print("L: {}".format(L))
    #print("R: {}".format(R))
    # Start comparing the sequences in L and R
    # Put them back into A
    i = 0
    j = 0
    for k in range(p,r+1):
        #print("i: {}, j: {}, k: {}".format(i,j,k))
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    #print("A: {}".format(A))

def mergeSort(A,p,r):
    #print (A,p,r)
    if p < r:
        q = int((p+r)/2)
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)
    

print("-"*25)
print("Merge Sort")
log.logStart()
mergeSort(A,0,len(A)-1)
#print(A)
log.logEnd()
print("-"*25)
    