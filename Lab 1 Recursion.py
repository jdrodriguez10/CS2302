# -*- coding: utf-8 -*-
"""
CS 2302 Data Structures
Author: John Rodriguez
Lab1 Recursion
Instructor: Olac Fuentes
TA: Anindita Nath
Date: 9/6/19
Purpose: create a program that uses recursion to
find the anagrams for a word using a text file
"""
from collections import Counter
import time

# function that reads words from file into a set
def read_words(file_name):
    words_set = set(line.strip() for line in open(file_name))
    return words_set


# function that finds the anagrams for a word
def anagrams(word, words_set):
    found_anagrams = []#list to store the anagrams of the users word
    counter_word = Counter(word)#stores the letters and the amount of each for the user's word
    for other_word in words_set:
        if Counter(other_word) == counter_word:#checks is there are the same letters/amount of specific letters in both strings
            found_anagrams.append(other_word)#adds that word to the found_anagrams list
    if word in found_anagrams: found_anagrams.remove(word)#removes user's word from anagrams
    found_anagrams.sort()#alphabetically sorts the anagrams
    print("The word ", word, " has the following ", len(found_anagrams), " anagrams:")
    return found_anagrams


# Main Function
try:#used to catch if the text file is not found
    words = read_words('words_alpha.txt')#stores the words on the text file into the variable words
    i = 0#used for the while loop
    while i <= 0:
        print('Enter a word or empty string to finish:')
        user_word = input()
        if (user_word == ""):
            print('Bye, thanks for using this program!')
            i = 1#exits out of loop
        else:    
            start = time.time()#starts the timer
            print(anagrams(user_word.lower().strip(), words))#executes the anagrams function
            end = time.time()#ends the timer
            print("It took ", (end - start), " seconds to find the anagrams")
except:
    print('The file was not found, make sure the spelling is correct or if it is in the same directory as the program')