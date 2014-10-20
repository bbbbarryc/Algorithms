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
    print (endTime - startTime)
    
# Start here 
A = [5,2,4,6,1,3]
A = [31, 41, 59, 26, 41, 58]
logStart()
A = [random.randint(1,100) for x in range(10000)]
logEnd()

# Takes 8s for range(10000)

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
    
    
def insertionSortDecreasing(A):
    #print("In: " + str(A))

    for j in range(1,len(A)):
        key = A[j]
        # Insert A[j] into sorted array A[0..j-1]
        i = j-1
        while i>=0 and A[i]<key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
        #print("Mid:" + str(A))
    
    #print("Out:" + str(A))
    

    
print("Increasing:")
logStart()
insertionSort(A[:])
logEnd()
print("-"*25)


print("Decreasing")
logStart()
insertionSortDecreasing(A[:])
logEnd()
print("-"*25)



