# -*- coding: utf-8 -*-
"""
CS 2302 Data Structures
Author: John Rodriguez
Lab 7
Instructor: Olac Fuentes
TA: Anindita Nath
Date: 12/8/19
Description: For lab 7 we had to use 3 diffrent alforithm design techniqes.
For part 1 we had to solve the Hamilton cycle using randomization and for
part 2 sovle it using backtracking. Part 3 focused on dynamic programing where
we had to modify the edit distance function to allow replacements only in the
case where the characters being interchanged are both vowels, or both consonants.
"""
import time
import numpy as np
import dsf
import graph_AL as AL
import graph_EL as EL
import random


# connected components function given by professor
def connected_components(g):
    vertices = len(g.al)
    components = vertices
    s = dsf.DSF(vertices)
    for v in range(vertices):
        for edge in g.al[v]:
            components -= s.union(v,edge.dest)
    return components


# function that returns the number of in-degrees for a vertex
def in_degree(G, v):
	indegree = 0
	for i in range(len(G.al)):
		for j in G.al[i]:
			if j.dest == v:
				indegree = indegree + 1
	return indegree


# function that returns if a Hamiltonian cycle using randomization
def randomized_hamiltonian(V, test_range):
    edge_list = V.as_EL()
    for t in range(test_range):
        edge = random.sample(edge_list.el, len(V.al)) # random edge from EL
        # inserts random edges into AL
        al = AL.Graph(len(V.al), weighted = V.weighted, directed = V.directed)
        for i in range(len(edge)):
            al.insert_edge(edge[i].source, edge[i].dest)
        if connected_components(al) == 1:
            for i in range(len(al.al)):
                if in_degree(al, i) != 2:
                    return False
            return True
        
        
# test function for randomized hamiltonian cycle
def randomized_hamiltonian_test(V, test_range):
    for i in range(100):
        if randomized_hamiltonian(V, test_range) == True:
            return "graph is a Hamiltonian Cycle"
    return "graph is not a Hamiltonian Cycle"


# helper function for hamiltonian cycle using backtracking
def help_backtrack(V, E):
	if len(V.el) == V.vertices:
		graphAL = V.as_AL()
		if connected_components(graphAL) == 1:
			for i in range(len(graphAL.al)):
				if in_degree(graphAL, i) != 2: #checks for in-degree of 2
					return None
			return graphAL
	if len(E) == 0:
		return
	else:
		V.el = V.el + [E[0]] 
		a = help_backtrack(V,E[1:])
		if a is not None:
			return a
		V.el.remove(E[0])
		return help_backtrack(V, E[1:])


# backtracking hamiltonian cycle function
def backtrack_hamiltonian(V):
    E = V.as_EL()
    el = EL.Graph(len(V.al), weighted=V.weighted, directed=V.directed)
    return help_backtrack(el,E.el)


# backtracking Hamiltonian cycle test
def backtrack_hamiltonian_test(V):
    h = backtrack_hamiltonian(V)
    if isinstance(h, AL.Graph):
        h.display()
        return "graph is a Hamiltonian Cycle"
    else:
        return "graph is not a Hamiltonian Cycle"
    

# edit distance function edited to only allow replacements with both vowels or both consonants
def edit_distance_modified(s1, s2):
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[0,:] = np.arange(len(s2)+1)
    d[:,0] = np.arange(len(s1)+1)
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                d[i,j] = d[i-1,j-1]
            else:
                # checks if both are vowels or both are consonants
                if (s1[i-1] in vowels and s2[j-1] in vowels) or (s1[i-1] not in vowels and s2[j-1] not in vowels):
                    n = [d[i,j-1], d[i-1,j-1], d[i-1,j]]
                    d[i,j] = min(n)+1
                else:
                    n = [d[i,j-1], d[i-1,j]]
                    d[i,j] = min(n)+1
    return d[-1,-1]
    

# Program Driver
print("Enter 1 to test Randomized Hamiltonian cycle")
print("Enter 2 to test Backtracking Hamiltonian cycle")
print("Enter 3 to test modified Edit Distance function")
user_selection = int(input())
if (user_selection == 1):
    # Hamiltonian Cycle Graph
    g1 = AL.Graph(5)
    g1.insert_edge(0, 1)
    g1.insert_edge(1, 2)
    g1.insert_edge(2, 3)
    g1.insert_edge(3, 4)
    g1.insert_edge(4, 0)
    g1.draw()
    # No Hamiltonian Cycle Graph
    g2 = AL.Graph(5)
    g2.insert_edge(0, 1)
    g2.insert_edge(0, 3)
    g2.insert_edge(1, 2)
    g2.insert_edge(2, 3)
    g2.insert_edge(3, 4)
    g2.draw()
    
    start_time = time.time() #starts timer
    print("Graph 1", randomized_hamiltonian_test(g1, 100))
    print("Graph 2", randomized_hamiltonian_test(g2, 100))
    run_time = (time.time() - start_time)
    print()
    print("Running Time for Randomized Hamiltonian Cycle Tests", run_time, "seconds")

if (user_selection == 2):
    # Hamiltonian Cycle Graph
    g1 = AL.Graph(5)
    g1.insert_edge(0, 1)
    g1.insert_edge(1, 2)
    g1.insert_edge(2, 3)
    g1.insert_edge(3, 4)
    g1.insert_edge(4, 0)
    g1.draw()
    # No Hamiltonian Cycle Graph
    g2 = AL.Graph(5)
    g2.insert_edge(0, 1)
    g2.insert_edge(0, 3)
    g2.insert_edge(1, 2)
    g2.insert_edge(2, 3)
    g2.insert_edge(3, 4)
    g2.draw()
        
    start_time = time.time() #starts timer
    print("Graph 1", backtrack_hamiltonian_test(g1))
    print("Graph 2", backtrack_hamiltonian_test(g2))
    run_time = (time.time() - start_time)
    print()
    print("Running Time for Backtrack Hamiltonian Cycle Tests", run_time, "seconds")

if (user_selection == 3):
    print("Enter first word")
    user_word1 = str(input())
    print("Enter second word")
    user_word2 = str(input())
    start_time = time.time() #starts timer
    print("modified edit distance:", edit_distance_modified(user_word1, user_word2))
    run_time = (time.time() - start_time)
    print()
    print("Running Time for Modified Edit Distance Test", run_time, "seconds")