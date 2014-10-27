#!/usr/bin/env python
# 2.1 - Insertion Sort
# p.18
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
    print "Time: " + str(endTime - startTime)
    
# Start here 
A = [5,2,4,6,1,3]
A = [31, 41, 59, 26, 41, 58]
logStart()
A = [random.randint(1,100) for x in range(10000)]
logEnd()

# Takes 2.5s to sort range(10000) (Ubuntu)

def selectionSort(A):
    #print("In: " + str(A))

    for i in range(len(A)-1):
        key = A[i]
        index = i # Keeps track of the position of the smallest element
        minVal = A[i]
        for j in range(i+1,len(A)):
            if A[j] < minVal:
                index = j
                minVal = A[j]
        A[i] = minVal # Loop invariant at the beginning of the loop
        A[index] = key # Swap the two values
        #print("Mid:" + str(A))
    
    #print("Out:" + str(A))

def selectionSortFromText(A):
    #print("In: " + str(A))

    for i in range(len(A)-1):
        minVal = i
        for j in range(i+1,len(A)):
            if A[j] < A[minVal]:
                minVal = j
        A[j],A[minVal] = A[minVal],A[j]
        #print("Mid:" + str(A))
    
    #print("Out:" + str(A))
    
print("-"*25)
print("Selection Sort")
logStart()
selectionSort(A[:])
logEnd()
print("-"*25)

print("Selection Sort From Text")
logStart()
selectionSortFromText(A[:])
logEnd()
print("-"*25)