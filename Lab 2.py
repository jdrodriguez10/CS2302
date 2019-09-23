# -*- coding: utf-8 -*-
"""
CS 2302 Data Structures
Author: John Rodriguez
Lab 2
Instructor: Olac Fuentes
TA: Anindita Nath
Date: 9/22/19
Purpose: use sorting algorithoms, bubble sort and difftent variations of quick sort to order a list
and return index k in that list after it's sorted
"""
import time
# Bubble Sort Function
def select_bubble(L,k):
    # condition that checks if the parameteres are valid
    if (k < 0) or (k >= len(L)) or (len(L) <= 0):
        return -1
    # loop that checks if the next number in the list is smaller then the current number
    # and switches the two numbers if it is smaller
    for i, num in enumerate(L):
        try:
            if L[i + 1] < num:
                L[i] = L[i + 1]
                L[i + 1] = num
                select_bubble(L,k) # uses recursion to go threw list until sorted
        except IndexError:
            pass
    return L[k]
    


# Partition Function used for Quick Sort
def partition(L,low,high):
    i = ( low-1 ) #i given value of low in the list
    pivot = L[high]
    for j in range(low, high):
        # if the number is smaller than the pviot it is placed to the left
        if L[j] < pivot:
            i = i + 1
            L[i], L[j] = L[j], L[i]
    # else it is larger than the pivot and placed to the right       
    L[i+1], L[high] = L[high], L[i+1] 
    return (i + 1)
    
    

# Quick Sort Function uses Recursion
def select_quick(L,low,high,k):
    if (k < 0) or (k >= len(L)) or (len(L) <= 0):
        return False
    if low < high:
        pivot = partition(L, low, high)
        select_quick(L, low, (pivot-1), k)# items in the list that are smaller than the 
        select_quick(L, (pivot+1), high, k)# items in the list that are larger then the pivot
    return L[k]
    


# Quick Sort Function sorts only the left or right of pivot deppending on value of k
def select_modified_quick(L,low,high,k):
    if (k < 0) or (k >= len(L)) or (len(L) <= 0):
        return False
    if low < high:
        pivot = partition(L, low, high)
        # if will only order items in the list that are smaller than the value of k
        if k < pivot:
            select_modified_quick(L, low, (pivot-1), k)
        # else will only order items in the list that are larger or equal to k
        else:
            select_modified_quick(L, (pivot+1), high, k)
    return L[k]
    


# Quick Sort Function that uses a stack instead of recursion
def stack_select_quick(L, k):
    # makes a stack 
    high = len(L) - 1 # hold the index of the high
    low = 0 # holds the index of the low
    size = (high + 1) - low # size of the stack
    stack = [0] * (size) 
    top = -1 #holds the index for the top of the stack
    # this pushes the initial values of the low and high
    top = top + 1
    stack[top] = low 
    top = top + 1
    stack[top] = high
    # this pops from stack until it's empty
    while top >= 0: 
        high = stack[top] 
        top = top - 1
        low = stack[top] 
        top = top - 1
        pivot = partition(L, low, high)  
        # pushes numbers to the left of the pivot to the left of the stack
        if (pivot - 1) > low: 
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = pivot - 1
        # pushes numbers to the right of the pivot to the right of the stack
        if pivot + 1 < high: 
            top = top + 1
            stack[top] = pivot + 1
            top = top + 1
            stack[top] = high
    return L[k]
        



# Main
a = 3
#Lists to test if functions work
test1_a = [55, 50, 130, 20, 100, 25, 70, 125, 35, 135, 80, 45, 10, 105, 5, 85, 60, 115, 65, 110, 90, 30, 75, 40, 120, 95, 15, 140]
test1_b = [55, 50, 130, 20, 100, 25, 70, 125, 35, 135, 80, 45, 10, 105, 5, 85, 60, 115, 65, 110, 90, 30, 75, 40, 120, 95, 15, 140]
test1_c = [55, 50, 130, 20, 100, 25, 70, 125, 35, 135, 80, 45, 10, 105, 5, 85, 60, 115, 65, 110, 90, 30, 75, 40, 120, 95, 15, 140]
test1_d = [55, 50, 130, 20, 100, 25, 70, 125, 35, 135, 80, 45, 10, 105, 5, 85, 60, 115, 65, 110, 90, 30, 75, 40, 120, 95, 15, 140]


#bubble sort
print('Bubble Sort')
print("list unsorted")
print(test1_a)
print()
start = time.time()#starts the timer
print(select_bubble(test1_a, a), " is the", (a + 1), "th smallest element in the list")
end = time.time()#ends the timer
print("It took ", (end - start), " seconds to sort")
print()
print("list sorted")
print(test1_a)
print()
print()


#quick sort
print('Quick Sort')
print("list unsorted")
print(test1_b)
print()
start = time.time()#starts the timer
print(select_quick(test1_b, 0, (len(test1_b) - 1), a), " is the", (a + 1), "th smallest element in the list")
end = time.time()#ends the timer
print("It took ", (end - start), " seconds to sort")
print()
print("list sorted")
print(test1_b)
print()
print()


#modified quick sort
print('Modified Quick Sort')
print("list unsorted")
print(test1_c)
print()
start = time.time()#starts the timer
print(select_modified_quick(test1_c, 0, (len(test1_c) - 1), a), " is the", (a + 1), "th smallest element in the list")
end = time.time()#ends the timer
print("It took ", (end - start), " seconds to sort")
print()
print("modified list")
print(test1_c)
print()
print()


#quick sort using a stack
print('Quick Sort using Stack')
print("list unsorted")
print(test1_d)
print()
start = time.time()#starts the timer
print(stack_select_quick(test1_d, a), " is the", (a + 1), "th smallest element in the list")
end = time.time()#ends the timer
print("It took ", (end - start), " seconds to sort")
print()
print("list sorted")
print(test1_d)
print()
print()
