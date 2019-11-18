# -*- coding: utf-8 -*-
"""
CS 2302 Data Structures
Author: John Rodriguez
Lab 6
Instructor: Olac Fuentes
TA: Anindita Nath
Date: 11/17/19
Purpose: For this lab we were tasked to create functiontions to build, modify, and display graphs for a adjacency matrix and an
edge list using functiontions given to us for a adjacency list. For the second part of the lab we were given the task to
solve a problem using a depth first search and a breadth first search.
"""
# Adjacency list representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AM as AM
import graph_EL as EL

class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
    
    # insert edge function given by professor
    def insert_edge(self,source,dest,weight=1):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        if weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest,weight)) 
            if not self.directed:
                self.al[dest].append(Edge(source,weight))
                
    # delete edge function given by professor
    def delete_edge_(self,source,dest):
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i+=1    
        return False
    
    # delete edge function given by professor
    def delete_edge(self,source,dest):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            deleted = self.delete_edge_(source,dest)
            if not self.directed:
                deleted = self.delete_edge_(dest,source)
        if not deleted:        
            print('Error, edge to delete not found')  
            
    # display function given by professor
    def display(self):
        print('[',end='')
        for i in range(len(self.al)):
            print('[',end='')
            for edge in self.al[i]:
                print('('+str(edge.dest)+','+str(edge.weight)+')',end='')
            print(']',end=' ')    
        print(']')   
    
    #draw function given by professor
    def draw(self):
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(self.al)):
            for edge in self.al[i]:
                d,w = edge.dest, edge.weight
                if self.directed or d>i:
                    x = np.linspace(i*scale,d*scale)
                    x0 = np.linspace(i*scale,d*scale,num=5)
                    diff = np.abs(d-i)
                    if diff == 1:
                        y0 = [0,0,0,0,0]
                    else:
                        y0 = [0,-6*diff,-8*diff,-6*diff,0]
                    f = interp1d(x0, y0, kind='cubic')
                    y = f(x)
                    s = np.sign(i-d)
                    ax.plot(x,s*y,linewidth=1,color='k')
                    if self.directed:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.plot(xd,yd,linewidth=1,color='k')
                    if self.weighted:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
            ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off') 
        ax.set_aspect(1.0)
        
    # functiontion that returns the edge list representation
    def as_EL(self):
        edge_list = EL.Graph(len(self.al), self.weighted, self.directed) # makes a EL graph that is same size as AL graph
        for i in range(len(self.al)):
            for j in self.al[i]:
                edge_list.insert_edge(i, j.dest, j.weight) # inserts edges
        return edge_list
    
    # functiontion that returns the adjacency matrix representation
    def as_AM(self):
        matrix =  AM.Graph(len(self.al), self.weighted, self.directed) # makes a AM graph that is same size as AL graph
        for i in range(len(self.al)):
            for j in self.al[i]:
                matrix.insert_edge(i, j.dest, j.weight) # inserts edges
        return matrix
    
    # functiontion that returns the adjacency list representation
    def as_AL(self):
        return self
    
    # functiontion that returns the path of a breadth first search
    def BFS(self, s, end): 
        visited = [False] * (len(self.al))
        queue = [[s]] 
        while queue: 
            s = queue.pop(0)
            if s[-1] == end: 
                print("Adjacency List BFS")
                return s
            for i in self.al[s[-1]]: 
                if visited[i.dest] == False: 
                    queue.append(s + [i.dest]) # appends if not visited
                    visited[i.dest] = True # marks visisted
    
    # functiontion that returns the path of a depth first search
    def DFS(self, s, end):
        visited = []
        print("Adjacency List DFS")
        return self.DFS_Util(visited, s, end)
    
    # DFS utility functiontion
    def DFS_Util(self, visited, s, end):
        if s not in visited:
            if len(visited) > 0 and visited[-1] == end:
                return
            visited.append(s) # s is appended to visited list
            for i in self.al[s]:
                self.DFS_Util(visited, i.dest, end)
        return visited
    
    # functiontion that prints the path
    def path_steps(self, function):
        if function == "DFS":
            search_path = self.DFS(0, len(self.al)-1)
        if function == "BFS":
            search_path = self.BFS(0, len(self.al)-1)
        for i in search_path:
            print (i, [int(x) for x in list("{0:04b}".format(i))]) 