# -*- coding: utf-8 -*-
"""
CS 2302 Data Structures
Author: John Rodriguez
Lab 5
Instructor: Olac Fuentes
TA: Anindita Nath
Date: 11/4/19
Purpose: Compare the run times between hash tables with one using chaining and the other using linear probing when
retrieving word embeddings to compare two given words. Then compare to the best running time when using a tree from lab 4.
"""
import numpy as np
import time

class WordEmbedding(object):
    def __init__(self, word, embedding):
        # word must be a string, embedding can be a list or and array of ints or floats
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32) # len(embedding=50)


class HashTableLP(object):
    # Builds a hash table of size 'size', initilizes items to -1 (which means empty)
    # Constructor
    def __init__(self, size):  
        self.item = np.zeros(size,dtype=np.object)-1
    
    # a hash function with length of string k % size of table for linear probing
    def length_word_hash_LP(self, k):
        if isinstance(k, WordEmbedding):
            k = k.word
        return len(k) % len(self.item)
    
    # a hash function that has the ASCII value of the first character of k % size of table for linear probing
    def ascii_first_hash_LP(self, k):
        if isinstance(k, WordEmbedding):
            k = k.word
        return ord(k[0]) % len(self.item)
        
    # a hash function that has the product of ASCII values from first and last char % size of table for linear probing
    def ascii_product_hash_LP(self, k):
        if isinstance(k, WordEmbedding):
            k = k.word
        return (ord(k[0]) * ord(k[-1])) % len(self.item)   
        
    # a hash function that has the sum of the ASCII values in k % size of table for linear probing  
    def ascii_sum_hash_LP(self, k):
        if isinstance(k, WordEmbedding):
            k = k.word
        return sum(map(ord, k)) % len(self.item)
        
    # a recursive hash function that multiplies the ASCII values of all the characters in k + 255 on each value % size of table for linear probing
    def recursive_hash_LP(self, k):
        if isinstance(k, WordEmbedding):
            k = k.word
        if len(k) == 0:
            return 1
        return (ord(k[0]) + 255 * self.recursive_hash_LP(k[1:])) % len(self.item)
    
    # a hash function that has the ASCII value of the last character of k % size of table for linear probing
    def custom_hash_LP(self,  k):
        if isinstance(k, WordEmbedding):
            k = k.word
        return ord(k[-1]) % len(self.item)
    
    # uses the hash function the user selects
    def h(self, k, selection): 
        if selection == 1:
            return self.length_word_hash_LP(k)
        if selection == 2:
            return self.ascii_first_hash_LP(k)
        if selection == 3:
            return self.ascii_product_hash_LP(k)
        if selection == 4:
            return self.ascii_sum_hash_LP(k)
        if selection == 5:
            return self.recursive_hash_LP(k)
        if selection == 6:
            return self.custom_hash_LP(k)
    
    # function to insert into a hash table using linear probing
    def insert(self, k, selection):
        start = self.h(k.word, selection)
        for i in range(len(self.item)):
            pos = (start + i) % len(self.item)
            if isinstance(self.item[pos], WordEmbedding):
                if self.item[pos].word == k.word:
                    return -1
            elif self.item[pos] < 0:
                self.item[pos] = k
                return pos
    
    # returns the embedding of the searched key if found
    def find_word_embedding(self, k, selection):
        try:
            if isinstance(k, WordEmbedding):
                k = k.word
            start = self.h(k, selection)
            for i in range(len(self.item)):
                pos = (start + i) % len(self.item)
                try:
                    if self.item[pos].word == k:
                        return self.item[pos].emb
                except AttributeError:
                    if self.item[pos]<0:
                        return None
        except TypeError:
            return


class HashTableChain(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self, size):  
        self.bucket = [[] for i in range(size)]
        
    # a hash function with length of string k % size of table for chanining
    def length_word_hash_C(self, k):
        if isinstance(k, WordEmbedding):
            k = k.word
        return len(k) % len(self.bucket)
    
    # a hash function that has ASCII value of the first character of k % size of table for chanining
    def ascii_first_hash_C(self, k):
        if isinstance(k, WordEmbedding):
            k = k.word
        return ord(k[0]) % len(self.bucket)
    
    # a hash function that has product of ASCII values from first and last char % size of table for chanining
    def ascii_product_hash_C(self, k):
        if isinstance(k, WordEmbedding):
            k = k.word
        return (ord(k[0]) * ord(k[-1])) % len(self.bucket)
    
    # a hash function that has the sum of the ASCII values in k % size of table for chanining
    def ascii_sum_hash_C(self, k):
        if isinstance(k, WordEmbedding):
            k = k.word
        return sum(map(ord, k)) % len(self.bucket)
    
    # a recursive hash function that multiplies the ASCII values of all the characters in k + 255 on each value % size of table for chanining
    def recursive_hash_C(self, k):
        if isinstance(k, WordEmbedding):
            k = k.word
        if len(k) == 0:
            return 1
        return (ord(k[0]) + 255 * self.recursive_hash_C(k[1:])) % len(self.bucket)
    
    # a hash function that has ASCII value of the last character of k % size of table for chaining
    def custom_hash_C(self, k):
        if isinstance(k, WordEmbedding):
            k = k.word
        return ord(k[-1]) % len(self.bucket)
    
    # uses the hash function the user selects
    def h(self, k, selection):
        if selection == 1:
            return self.length_word_hash_C(k)
        if selection == 2:
            return self.ascii_first_hash_C(k)
        if selection == 3:
            return self.ascii_product_hash_C(k)
        if selection == 4:
            return self.ascii_sum_hash_C(k)
        if selection == 5:
            return self.recursive_hash_C(k)
        if selection == 6:
            return self.custom_hash_C(k)
    
    # function to insert into a hash table using chaining
    def insert(self, k, selection):
        b = self.h(k, selection)
        if not k in self.bucket[b]:
            self.bucket[b].append(k)
    
    # returns the embedding of the searched key if found
    def find_word_embedding(self, k, selection):
        b = self.h(k, selection)
        for n in self.bucket[b]:
            if n.word == k:
                return n.emb
        return
        
        
# checks if a string only contains letters
def only_letters(string):
    for letter in string:
        if letter.lower() not in "abcdefghijklmnopqrstuvwxyz":
            return False
    return True

# returns the diffrence between two words using the words embedding
def words_diffrence(a, b):
    if a is None or b is None:
        return
    diffrence = np.dot(a, b)/(np.linalg.norm(a)* np.linalg.norm(b))
    return diffrence


#Driver
menu = 0 # used to stay in the menu until one of the two choices are picked
while menu <= 0:
    print("Choose table implementation")
    print("Type 1 for hash table using chaining or 2 for hash table using linear probing:")
    choice = input() # the users input for the menu choice
    print("Choice:", choice)
    print()
    
    if choice == "1":
        print("Type 1 for the length of the string % n")
        print("Type 2 for the ascii value (ord(c)) of the first character in the string % n")
        print("Type 3 for the product of the ascii values of the first and last characters in the string % n")
        print("Type 4 for the sum of the ascii values of the characters in the string % n")
        print("Type 5 for recursive function h(”,n) = 1; h(S,n) = (ord(s[0]) + 255*h(s[1:],n))% n")
        print("Type 6 for the Custom function")
        print("Select a hash function:")
        selection = int(input())
        print("Selection:", selection)
        print()
        print("Building hash table with chaining")
        print()
        file = open('glove.6B.50d.txt', encoding = "utf8") # opens the glove.6B.50d file
        table_size = 56432
        H = HashTableChain(table_size)
        
        start_time = time.time() #starts timer
        for line in file.readlines():
            try:
                row = line.strip().split(' ')
                word = row[0] # stores the word from the file
                if only_letters(word) is True: # checks if the word only contains letters  
                    H.insert(WordEmbedding(word, [(i) for i in row[1:]]), selection) # inserts the word and it's embedding into the hash table
            except TypeError:
                e = 2 # does noting so it can move to the next line in the file
        run_time = (time.time() - start_time) #ends timer and stores the result in run_time
        
        print("Hash table stats:")
        print("Hash table size:", table_size)
        print("Running time for hash table construction:", "%s seconds" % run_time) # outputs the running time of the hash table construction
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
                print("Similarity:",word1, word2, "=", words_diffrence((H.find_word_embedding(word1, selection)), (H.find_word_embedding(word2, selection))))
            except IndexError:
                e = 2
        run_time = (time.time() - start_time) # stores the running time for the hash table query in run_time
        
        print()
        print("Running time for hash table query processing:", "%s seconds" % run_time)
        menu = 5 #Exits the while loop
            
         
    elif choice == "2":
        print("Type 1 for the length of the string % n")
        print("Type 2 for the ascii value (ord(c)) of the first character in the string % n")
        print("Type 3 for the product of the ascii values of the first and last characters in the string % n")
        print("Type 4 for the sum of the ascii values of the characters in the string % n")
        print("Type 5 for recursive function h(”,n) = 1; h(S,n) = (ord(s[0]) + 255*h(s[1:],n))% n")
        print("Type 6 for the Custom function")
        print("Select a hash function:")
        selection = int(input())
        print("Selection:", selection)
        print()
        print("Building hash table with linear probing")
        print()
        file = open('glove.6B.50d.txt', encoding = "utf8") # opens the glove.6B.50d file
        table_size = 100 # I made the table size 100 for the hash table using linear probing to show it works because it takes too long with a larger size
        H = HashTableLP(table_size)
        
        start_time = time.time() #starts timer
        for line in file.readlines():
            try:
                row = line.strip().split(' ')
                word = row[0] # stores the word from the file
                if only_letters(word) is True: # checks if the word only contains letters  
                    H.insert(WordEmbedding(word, [(i) for i in row[1:]]), selection) # inserts the word and it's embedding into the hash table
            except TypeError:
                e = 2 # does noting so it can move to the next line in the file
        run_time = (time.time() - start_time) #ends timer and stores the result in run_time
        
        print("Hash table stats:")
        print("Hash table size:", table_size)
        print("Running time for hash table construction:", "%s seconds" % run_time) # outputs the running time of the hash table construction
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
                print("Similarity:",word1, word2, "=", words_diffrence((H.find_word_embedding(word1, selection)), (H.find_word_embedding(word2, selection))))
            except IndexError:
                e = 2
        run_time = (time.time() - start_time) # stores the running time for the hash table query in run_time
        
        print()
        print("Running time for hash table query processing:", "%s seconds" % run_time)
        menu = 5 #Exits the while loop
        
        
    else: # used if the user doesnt input 1 or 2 as their choice
        print("Please select between 1 or 2")
        print()   