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
import matplotlib.pyplot as plt
import numpy as np
import graph_AL as AL
import graph_AM as AM
import graph_EL as EL

# tests will be performed on the type of graph the user selects
def GraphTest(selection):
    if selection == 1:
        graph = AL
    elif selection == 2:
        graph = AM
    elif selection == 3:
        graph = EL
    
    print("Unweighted and Undirected")
    g = graph.Graph(6)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    print()
    
    print("Unweighted and Directed")
    g = graph.Graph(6,directed = True)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    print()
    
    print("Weighted and Undirected")
    g = graph.Graph(6,weighted=True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    print()
    
    print("Weighted and Directed")
    g = graph.Graph(6,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    print()
    
    print("As Adjacency List")
    g1 = g.as_AL()
    g1.draw()
    g1.display()
    print()
    
    print("As Adjacency Matrix")
    g2 = g.as_AM()
    g2.draw()
    g2.display()
    print()
    
    print("As Edge List")
    g3 = g.as_EL()
    g3.draw()
    g3.display()