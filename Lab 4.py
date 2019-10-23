# -*- coding: utf-8 -*-
"""
CS 2302 Data Structures
Author: John Rodriguez
Lab 4
Instructor: Olac Fuentes
TA: Anindita Nath
Date: 10/22/19
Purpose: Compare the run times between B-Trees and Binary Search Trees when
retrieving word embeddings to compare two given words.
"""
import time
import numpy as np

class BST(object):
    # Constructor
    def __init__(self, data, left=None, right=None):  
        self.data = data
        self.left = left 
        self.right = right
        


class BTree(object):
    # Constructor
    def __init__(self,data,child=[],isLeaf=True,max_data=5):  
        self.data = data
        self.child = child 
        self.isLeaf = isLeaf
        if max_data <3: #max_data must be odd and greater or equal to 3
            max_data = 3
        if max_data%2 == 0: #max_data must be odd and greater or equal to 3
            max_data +=1
        self.max_data = max_data
        
        
        
class WordEmbedding(object):
    def __init__(self, word, embedding):
        # word must be a string, embedding can be a list or and array of ints or floats
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32) # For Lab 4, len(embedding=50)
        
        
# Inserts a node into the binary search tree
def Insert_BST(T,newdata):
    if T == None:
        T =  BST(newdata)
    elif T.data.word > newdata.word:
        T.left = Insert_BST(T.left,newdata)
    else:
        T.right = Insert_BST(T.right,newdata)
    return T


# searches the binary search tree for the key and returns that node if found
def Search_BST(T,key):
    if T is None or T.data.word == key:
        return T
    if T.data.word < key:
        return Search_BST(T.right,key)
    return Search_BST(T.left,key)
        

# returns the height of a binary search tree
def Height_BST(T): 
    if T is None: 
        return 0 ;  
    else :  
        l = Height_BST(T.left) 
        r = Height_BST(T.right) 
        if (l > r): 
            return l + 1
        else: 
            return r + 1


# returns the number of nodes found in the binary search tree
def Size_BST(T):
    if T is None:
        return 0
    else:
        return Size_BST(T.left) + Size_BST(T.right) + 1


def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.data.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)
        
        
def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
    if isinstance(k, WordEmbedding):
        for i in range(len(T.data)):
            if k.word < T.data[i].word:
                return i
    else:
        for i in range(len(T.data)):
            if k < T.data[i].word:
                return i
    return len(T.data)


def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    for i in range(len(T.data)):   
        if k in T.data[i].word:
            return T.data[i]
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)


def Split(T):
    mid = T.max_data//2
    if T.isLeaf:
        leftChild = BTree(T.data[:mid],max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],max_data=T.max_data) 
    else:
        leftChild = BTree(T.data[:mid],T.child[:mid+1],T.isLeaf,max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],T.child[mid+1:],T.isLeaf,max_data=T.max_data) 
    return T.data[mid], leftChild,  rightChild


def Leaves(T):
    # Returns the leaves in a b-tree
    if T.isLeaf:
        return [T.data]
    s = []
    for c in T.child:
        s = s + Leaves(c)
    return s
        
        
def InsertLeaf(T,i):
    T.data.append(i)  
    T.data.sort(key = lambda x: x.word)


# checks if the max_data has been reached yet
def IsFull(T):
    return len(T.data) >= T.max_data


# inserts a node into the B-Tree
def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.data =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)
        

def Set_x(T,Dx):
    # Finds x-coordinate to display each node in the tree
    if T.isLeaf:
        return 
    else:
        for c in T.child:
            Set_x(c,Dx)
        d = (Dx[T.child[0].data[0]] + Dx[T.child[-1].data[0]] + 10*len(T.child[-1].data))/2
        Dx[T.data[0]] = d - 10*len(T.data)/2


# returns the height of a B-Tree
def Height(T):
    if T.isLeaf:
        return 0
    return 1 + Height(T.child[0])


# returns the number of nodes in a B-Tree
def NumItems(T):
    num_items = len(T.data)
    if not T.isLeaf:
        for c in range(len(T.child)):
            num_items += NumItems(T.child[c])
    return num_items


# checks if a string only contains letters
def OnlyLetters(string):
    for letter in string:
        if letter.lower() not in "abcdefghijklmnopqrstuvwxyz":
            return False
    return True


# returns the diffrence between two words using the words embedding for BST
def words_diffrence(a, b):
    diffrence = np.dot(a.data.emb, b.data.emb)/(np.linalg.norm(a.data.emb)*np.linalg.norm(b.data.emb))
    return diffrence


# returns the diffrence between two words using the words embedding for B-Tree
def words_diffrence_BTree(a, b):
    diffrence = np.dot(a.emb, b.emb)/(np.linalg.norm(a.emb)*np.linalg.norm(b.emb))
    return diffrence


#Driver
menu = 0 # used to stay in the menu until one of the two choices are picked
while menu <= 0:
    print("Choose table implementation")
    print("Type 1 for binary search tree or 2 B-tree")
    choice = input() # the users input for the menu choice
    print("Choice:", choice)
    print()
    
    if choice == "1":
        print("Building binary search tree")
        print()
        file = open('glove.6B.50d.txt', encoding = "utf8") # opens the glove.6B.50d file
        T = None
        
        start_time = time.time() #starts timer
        for line in file.readlines():
            try:
                row = line.strip().split(' ')
                word = row[0] # stores the word from the file
                if OnlyLetters(word) is True: # checks if the word only contains letters
                    T = Insert_BST(T, WordEmbedding(word, [(i) for i in row[1:]])) # inserts the word and it's embedding into the tree
            except TypeError:
                e = 2 # does noting so it can move to the next line in the file
        run_time = (time.time() - start_time) #ends timer and stores the result in run_time
        
        print("Binary Search Tree stats:")
        print("Number of Nodes:", Size_BST(T)) # outputs the the number of nodes in the bst
        print("Height:", Height_BST(T)) # outputs the height of the bst
        print("Running time for binary search tree construction:", "%s seconds" % run_time) # outputs the running time of the bst construction
        print()
        print("Reading word file to determine similarities")
        print()
        file2 = open('word file.txt', encoding = "utf8")# opens the file word_file which contains the list of the set of words
        print("Word similarities found:")
        
        start_time = time.time() # starts the timer
        for line in file2.readlines():
            try:
                row = line.strip().split(' ')
                word1 = row[0]# holds the first word
                word2 = row[1]# holds the second word
                print("Similarity",word1, word2, "=", words_diffrence(Search_BST(T, word1), Search_BST(T, word2)))
            except IndexError:
                break
        run_time = (time.time() - start_time) # stores the running time for the bst query in run_time
        
        print()
        print("Running time for binary search tree query processing:", "%s seconds" % run_time)
        menu = 5 #Exits the while loop
            
        
        
    elif choice == "2":
        print("Enter the maximum number of items to store in a node")
        max_num = int(input()) #  holds the users input for the max_data of the B-Tree
        print("Maximum number of items in node:", max_num)
        print()
        print("Building B-tree")
        print()
        file = open('glove.6B.50d.txt', encoding = "utf8") # opens the file glove.6B.50d
        T = BTree([], [], max_data=max_num)
        
        start_time = time.time() #starts timer
        for line in file.readlines():
            try:
                row = line.strip().split(' ')
                word = row[0] # holds the word for the line in the file
                if OnlyLetters(word) is True: # checks if the word in the line contains only letters
                    Insert(T, WordEmbedding(word, [(i) for i in row[1:]])) # inserts the node into the B-Tree
            except TypeError:
                e = 2 # does nothing so it can move on to the next line in the file
        run_time = (time.time() - start_time) #ends timer and stores the result in run_time
        
        print("B-Tree stats:")
        print("Number of Nodes:", NumItems(T))
        print("Height:", Height(T))
        print("Running time for b-tree construction:", "%s seconds" % run_time) # output of the time for the B-Tree to construct
        print()
        print("Reading word file to determine similarities")
        print()
        file2 = open('word file.txt', encoding = "utf8") # opens the words file
        print("Word similarities found:")
        
        start_time = time.time() # starts the timer
        for line in file2.readlines():
            try:
                row = line.strip().split(' ')
                word1 = row[0] # holds the first word in the line
                word2 = row[1] # holds the second word in the line
                print("Similarity",word1, word2, "=", words_diffrence_BTree(Search(T, word1), Search(T, word2))) # outputs the similarity between the two words
            except IndexError:
                break
        run_time = (time.time() - start_time) # stops the timer and stores the result in run_time
        
        print()
        print("Running time for B-Tree query processing:", "%s seconds" % run_time)
        menu = 5 #Exits the while loop


    else: # used if the user doesnt input 1 or 2 as their choice
        print("Please select between 1 or 2")
        print()