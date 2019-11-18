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
# Edge list representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AM as AM
import graph_AL as AL

class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.el = []
        self.vertices = vertices
        self.weighted = weighted
        self.directed = directed
        self.representation = "EL"
    
    # insert edge function
    def insert_edge(self,source,dest,weight=1):
        if weight != 1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.el.append(Edge(source,dest,weight)) 

    # delete edge function
    def delete_edge(self,source,dest):
        for i in self.el:
            if i.source == source and i.dest == dest:
                self.el.remove(i)
    
    # functiontion that prints the edge list edges            
    def display(self):
        print('[',end='')
        for i in self.el:
            print('('+str(i.source)+','+str(i.dest)+','+str(i.weight)+')',end='')
        print(']',end=' ')
        print('')
    
    # changes to AL then draws the graph
    def draw(self):
        adjlist = self.as_AL()
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(adjlist.al)):
            for edge in adjlist.al[i]:
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
    
    # functiontiontion that returns the edge list representation
    def as_AM(self):
        matrix =  AM.Graph(self.vertices, self.weighted, self.directed)
        for i in self.el:
            matrix.insert_edge(i.source, i.dest, i.weight)
        return matrix
    
    # functiontiontion that returns the edge list representation
    def as_AL(self):
        adjlist =  AL.Graph(self.vertices, self.weighted, self.directed)
        for i in self.el:
            adjlist.insert_edge(i.source, i.dest, i.weight)
        return adjlist
    
    # functiontiontion that returns the edge list representation
    def as_EL(self):
        return self
    
    # functiontion that returns BFS path
    def BFS(self, s,end): 
        visited = [False] * (self.vertices)
        visited[s]=True
        queue = [[s]] 
        path=[s]
        while queue: 
            s = queue.pop(0)
            if s == end:
                return
            for i in self.el: 
                if visited[i.dest] == False: 
                    queue.append(i.dest)
                    visited[i.dest] = True
                    path.append(i.dest)
            print("Edge List BFS")      
            return path
    
    # functiontion that returns DFS path                 
    def DFS(self, s, end):
        visited = []
        print("Edge List DFS")
        return self.DFS_(visited, s, end)
    
    # DFS utility functiontiontion
    def DFS_(self, visited, s, end):
        if s not in visited:
            if len(visited) > 0 and visited[-1]==end:
                return
            visited.append(s)
            for i in self.el:
                self.DFS_(visited, i.dest, end)
        return visited
    
    # functiontiontion that prints the path 
    def path_steps(self, func):
        if func == "DFS":
            search_path = self.DFS(0,self.vertices-1)
        if func == "BFS":
            search_path = self.BFS(0,self.vertices-1)
        for i in search_path:
            print (i, [int(x) for x in list('{0:04b}'.format(i))])