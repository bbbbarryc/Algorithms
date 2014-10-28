#!/usr/bin/env python

import random
import BCLogging as log

A = [5, 2, 4, 6, 1, 3]
A = [51, 31, 41, 59, 26, 41, 58]
numRange = 10000
A = [random.randint(1,100) for x in range(numRange)]

def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        # Insert A[j] into sorted array A[0..j-1]
        i = j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    #return A
    
    
def binarySearch(A, st, en, key):
    if en-st == 1:
        if key < A[st]: # 1 element
            return st # less than (insert at st)
        if key >= A[st]: # greater than (insert at en)
            return en #alternatively: st+1
    else:
        mid = int((st+en)/2)
        if key < A[mid]: 
            return binarySearch(A, st, mid, key) # search lower half
        elif key > A[mid]:
            return binarySearch(A, mid, en, key) # search upper half
        else:
            return mid # Hit it right on; return this value
        
def insertionSortBinarySearch(A):
    p = 1 # Start on the second element (the first is our loop invariant)
    while p < len(A): # While we aren't at the end of the list
        key = A[p]      # Take the element beside the loop invariant
        q = binarySearch(A,0,p,key) # Find insert location
        r = p - 1 # counter 
        while r >= q:
            A[r+1] = A[r] # start shifting elements, starting with p (the key location)
            r = r - 1
        A[q] = key # Put the key into the right spot
        p = p + 1 # Increase the loop invariant by 1 each time
    #return A
    
A = [random.randint(1,100) for x in range(numRange)]
print("-"*25)
print("Insertion Sort {} elements: ".format(numRange))
log.logStart()
insertionSort(A)
#print(A)
log.logEnd()
print("-"*25)


A = [random.randint(1,100) for x in range(numRange)]
print("-"*25)
print("Insertion Sort Improved w/ Binary Search {} elements: ".format(numRange))
log.logStart()
insertionSortBinarySearch(A)
#print(A)
log.logEnd()
print("-"*25)


# insertionSort w/ 10000: 6.3s
# insertionSortBinarySearch w/ 10000: 5.4s

# insertionSort w/ 100000: 629s
# insertionSortBinarySearch w/ 100000: 543s

# Both are still O(n^2) but the binary search helps a bit.  
