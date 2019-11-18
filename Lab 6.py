# -*- coding: utf-8 -*-
"""
CS 2302 Data Structures
Author: John Rodriguez
Lab 6
Instructor: Olac Fuentes
TA: Anindita Nath
Date: 11/17/19
Purpose: For this lab we were tasked to create functions to build, modify, and display graphs for a adjacency matrix and an
edge list using functions given to us for a adjacency list. For the second part of the lab we were given the task to
solve a problem using a depth first search and a breadth first search.
"""
import graph_AL as AL
import graph_AM as AM
import graph_EL as EL
import test_graphs as test
import time

# Graph type menu
print("Select 1 for Adjacency List")
print("Select 2 for Adjacency Matrix")
print("Select 3 for Edge List")
user_graph_selection = int(input())
print()

# Lab part choice menu
print("Select 1 to run tests on graph type")
print("Select 2 for problem with the fox, chicken, grain, and farmer")
user_part_selection = int(input())
print()

# Runs test_graphs program
if user_part_selection == 1:
    start_time = time.time() #starts timer
    test.GraphTest(user_graph_selection)
    run_time = (time.time() - start_time)
    print()
    print("Running Time for Tests", run_time, "seconds")
    
# Starts part 2 of lab
elif user_part_selection == 2:
    if user_graph_selection == 1:
        g = AL.Graph(16)
    if user_graph_selection == 2:
        g = AM.Graph(16)
    if user_graph_selection == 3:
        g = EL.Graph(16)
    
    # inserts edges into graph
    g.insert_edge(0, 5)
    g.insert_edge(5, 4)
    g.insert_edge(4, 7)
    g.insert_edge(4, 13)
    g.insert_edge(2, 13)
    g.insert_edge(7, 11)
    g.insert_edge(10, 11)
    g.insert_edge(10, 15)
      
    # menu for the search type the user wants
    print("Select 1 for Breadth First Search")
    print("Select 2 for Depth First Search")
    user_search_selection = int(input())
    print()
    if user_search_selection == 1:
        start_time = time.time() #starts timer
        print(g.BFS(0, 15))
        print()
        g.path_steps("BFS")
        print()
    if user_search_selection == 2:
        start_time = time.time() #starts timer
        print(g.DFS(0, 15))
        print()
        g.path_steps("DFS")
        print()
    run_time = (time.time() - start_time)
    print("Running Time", run_time, "seconds")
    print()
    print("Drawing Graph")
    g.draw()