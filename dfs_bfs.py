#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 22:45:09 2018

@author: babavyas
"""

# Python program to check if a given directed graph is strongly 
# connected or not
 
from collections import defaultdict
  
#This class represents a directed graph using adjacency list representation
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
  
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
     
  
    #A function used by isSC() to perform DFS
    def DFSUtil(self,v,visited):
        print('before')
        print(visited)
        # Mark the current node as visited 
        visited[v]= True
        print('after')
        print(visited)
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                
                
                self.DFSUtil(i,visited)
                
    def BFS(self, s,visited):
 
        
        # Mark the current node as visited 
        
        
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as 
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from 
            # queue and print it
            s = queue.pop(0)
            #print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    print('before')
                    print(visited)
                    queue.append(i)
                    visited[i] = True
                    print('after')
                    print(visited)
    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
 
        g = Graph(self.V)
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
         
        return g
 
         
    # The main function that returns true if graph is strongly connected
    def isSC(self):
 
        # Step 1: Mark all the vertices as not visited (For first DFS)
        visited =[False]*(self.V)
         
        # Step 2: Do DFS traversal starting from first vertex.
        self.DFSUtil(0,visited)
 
        # If DFS traversal doesnt visit all vertices, then return false
        if any(i == False for i in visited):
            return False
 
        # Step 3: Create a reversed graph
        #gr = self.getTranspose()
         
        # Step 4: Mark all the vertices as not visited (For second DFS)
        visited =[False]*(self.V)
 
        # Step 5: Do DFS for reversed graph starting from first vertex.
        # Staring Vertex must be same starting point of first DFS
        #gr.DFSUtil(0,visited)
 
        # If all vertices are not visited in second DFS, then
        # return false
        #if any(i == False for i in visited):
        #    return False
        
        print('BFS TEST')
        self.BFS(0,visited)
        if any(i == False for i in visited):
            return False
        return True
 
# Create a graph given in the above diagram
g1 = Graph(5)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.addEdge(3, 0)
g1.addEdge(2, 4)
g1.addEdge(4, 2)
print ("Yes" if g1.isSC() else "No")
print('Second e.g.')
g2 = Graph(5)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
g2.addEdge(0, 4)
print ("Yes" if g2.isSC() else "No")


# bfs with level
'''
class Graph:
    def __init__(self,vertices,edges):
        self.graph = {}
        for v in range(vertices):
            self.graph[v] = []
        self.V = vertices
        self.E = edges

    def connect(self,x,y):
            self.graph[x].append(y)
            self.graph[y].append(x)
    
    def find_all_distances(self,s):
        
        q = []
        visited = [-1]*self.V
        q.append(s)
        visited[s] = 1
        level = [-1]*self.V
        level[s] = 0
        while q:
            r = q[0]
            del(q[0])
            
            for v in self.graph[r]:
                if visited[v] == -1:
                    visited[v] = 1
                    level[v] = level[r] + 6
                    q.append(v)
        
        del(l[s])
        res = ' '.join(map(str,l))
        print(res)


t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n,m)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    #print(graph.graph)
    s = int(input())
    graph.find_all_distances(s-1)
'''