# -*- coding: utf-8 -*-
"""
CS 2302 Data Structures
Author: John Rodriguez
Lab3
Instructor: Olac Fuentes
TA: Anindita Nath
Date: 10/6/19
Purpose: create a sorted linked list and implement the 10 functions described.
"""
import math
class Node(object):
    # Constructor
    def __init__(self, data, next=None):  
        self.data = data
        self.next = next 


class SortedList(object):   
    # Constructor
    def __init__(self,head = None,tail = None):    
        self.head = head
        self.tail = tail
    
    
    #Function that prints the entire list
    def Print(self):
        t = self.head
        while t is not None:
            print(t.data,end=' ')
            t = t.next
        print()
    
    
    #Function that inserts a element in the correct spot of the sorted list
    def Insert(self, i):
        new_node = Node(i)
        #if the list is empty the new node becomes the new head
        if self.head is None:
            self.head = new_node
            self.head.next = None
        #if the new node is a smaller element it becomes the new head
        elif self.head.data >= i:
            t = self.head
            self.head = new_node
            self.head.next = t
        #when the data value in the list is larger than the value of i the new node is inserted
        else:
            t = self.head
            while(t.next is not None and t.next.data < i):
                t = t.next
            new_node.next = t.next
            t.next = new_node
            
    
    #Function that deletes a element in the list if it is equal to the value of i
    def Delete(self, i):
        t = self.head
        #if the list is empty nothing happens
        if self.head is None:
            return None
        #if the head holds the value of i it is removed
        elif t.data == i:
            if t.next is None:
                self.head = None
            else:
                self.head = t.next
        #element is removed if it is found in the list
        else:
            prev = t
            while t is not None:
                if t.data == i:
                    prev.next = t.next
                prev = t
                t = t.next
    """
    #Function that merges two sorted lists
    def Merge(self, M):
        if self.head is None and M is None:
            return None
        if self.head is None:
            return M
        if M is None:
            return self
        new_list = SortedList()
        prev = new_list
        t = self.head
        r = M.head
        while self is not None and M is not None:
            if t.data <= r.data:
                prev.next = t
                t = t.next
            else:
                prev.next = r
                r = r.next
            prev = prev.next
        if t is None:
            prev.next = r
        elif r is None:
            prev.next = t
        return new_list
    """
    #Function that returns the index of i in the list
    def IndexOf(self, i):
        count = 0 #used to hold the current index
        t = self.head
        #if the list is empty -1 is returned
        if self.head is None:
            return -1
        #goes threw list until the element with the value of i is found and the index is returned
        else:
            while t is not None:
                if t.data == i:
                    return count
                t = t.next
                count = count + 1
            return -1 #if the value of i is not found -1 is returned
        
    
    #Function that clears the list
    def Clear(self):
        #if the list is empty nothing is happens
        if self.head is None:
            return self
        #makes the list empty
        self.head.next = None
        self.head = None
        
    
    #Function that returns the smallest element in the list
    def Min(self):
        #if the list is empty math.inf is returned
        if self.head is None:
            return math.inf
        return self.head.data #returns the head of list which is smallest element
    
    
    #Function that returns the largest element in the list
    def Max(self):
        t = self.head
        #if the list is empty -math.inf is returned
        if self.head is None:
            return -math.inf
        #if the list only has a head it's value is returned
        if self.head.next is None:
            return t.data
        #goes threw list until the last element is reached and that element is returned
        while t.next is not None:
            t = t.next
        return t.data
    
    
    #returns if the list has duplicates or not
    def HasDuplicates(self):
        t = self.head
        #if the list is empty or only has a head it returns false
        if t is None or t.next is None:
            return False
        #goes threw list and if a duplicate element is found true is returned
        while t.next is not None:
            if t.data == t.next.data:
                return True
            t = t.next
        return False #if the end of the list is reached and no duplicates found returns false
    
    
    #returns the kth smallest element in the list. k is given the value of a selected index
    def Select(self, k):
        t = self.head
        count = 0 #used as a referce to the index of the list
        #if the list is empty math.inf is returned
        if self.head is None:
            return math.inf
        #goes threw list until count is equal to k and returns the elemet in that index
        while t is not None:
            if count == k:
                return t.data
            t = t.next
            count = count + 1
        return math.inf #if k index is not found in the list
    
    
    
#Program Driver
#Tests for the Insert Function
print("Insert Function Test")
llist = SortedList()
llist.Insert(5)
llist.Print()
llist.Insert(10)
llist.Print()
llist.Insert(7)
llist.Print()
llist.Insert(3)
llist.Print()
llist.Insert(1)
llist.Print()
llist.Insert(9)
llist.Print()
llist.Insert(7)
llist.Print()
print()
print()


#Tests for the Delete Function
print("Delete Function Test")
llist.Delete(1)
llist.Print()
llist.Delete(7)
llist.Print()
print()
print()


"""
#Test for the Merge Function
print("Merge Function Test")
sec_llist = SortedList()
sec_llist.Insert(2)
sec_llist.Insert(6)
sec_llist.Insert(4)
print("first list contents")
llist.Print()
print("second list contents")
sec_llist.Print()
llist.Merge(sec_llist)
llist.Print()
print()
print()
"""


#Tests for the IndexOf Function
print("InexOf Function Test")
llist.Print()
print(llist.IndexOf(9), "is the index of 9 in the list")
print(llist.IndexOf(3), "is the index of 3 in the list")
print(llist.IndexOf(28), "is the index of 28 in the list")
print()
print()


#Tests for the Clear Function
print("Clear Function Test")
llist.Print()
llist.Clear()
llist.Print()
llist.Insert(25)
llist.Print()
llist.Clear()
llist.Print()
llist.Insert(5)
llist.Insert(15)
llist.Insert(10)
llist.Insert(25)
llist.Print()
print()
print()


#Tests for the Min Function
print("Min Function Test")
llist.Print()
print(llist.Min(), "is the smallest element in the list")
llist.Insert(1)
llist.Print()
print(llist.Min(), "is the smallest element in the list")
print()
print()


#Tests for the Max Function
print("Max Function Test")
llist.Print()
print(llist.Max(), "is the largest element in the list")
llist.Insert(55)
llist.Print()
print(llist.Max(), "is the largest element in the list")
print()
print()


#Tests for the HasDuplicate Function
print("HasDuplicate Test")
llist.Print()
print(llist.HasDuplicates())
llist.Insert(25)
llist.Print()
print(llist.HasDuplicates())
print()
print()


#Tests for the Select Function
print("Select Function Test")
llist.Print()
print(llist.Select(3), "is the 4th smallest element in the list")
print(llist.Select(25), "is the 26th smallest element in the list")
print()
print()


#Testing all Functions on Empty List except for Insert
empty_llist = SortedList()

print("Empty List Test")
empty_llist.Delete(5)
empty_llist.Print()
print(empty_llist.IndexOf(5))
empty_llist.Clear()
empty_llist.Print()
print(empty_llist.Min())
print(empty_llist.Max())
print(empty_llist.HasDuplicates())
print(empty_llist.Select(1))