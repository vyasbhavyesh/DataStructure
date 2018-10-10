#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:28:44 2018

@author: babavyas

"""

class Graph:
    def __init__(self,vertices):
        self.graph = {}
        self.V = vertices
        self.last = 0
        
    def add_edge(self,s,d):
        
        if s > self.V:
            print("Enter a valid source vertex")
            return
        if d > self.V:
            print("Enter a valid destination vertex")
            return
        
        if s not in self.graph.keys():
            self.graph[s] = [d]
            
        else:
            self.graph[s].append(d)
            

    def bfs(self, s):
        q = []
        print(s)
        visited = [s]
        q.append(s)
        
        while q :
            r = q[0]
            del(q[0])
            #print(self.graph[r])
            for v in self.graph[r]:
                if v not in visited:
                    print(v)
                    self.last = v
                    visited.append(v)
                    q.append(v)
        return self.last
    def corret(self):
        for i in range(self.V):
            if i not in self.graph.keys():
                self.graph[i] = []

g = Graph(13)
g.add_edge(0,1)
g.add_edge(0,4)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(4,5)
g.add_edge(4,9)
g.add_edge(5,6)
g.add_edge(5,7)
g.add_edge(7,8)
g.add_edge(9,10)
g.add_edge(9,11)
g.add_edge(11,12)

g.add_edge(1,0)
g.add_edge(4,0)
g.add_edge(2,1)
g.add_edge(3,1)
g.add_edge(5,4)
g.add_edge(9,4)
g.add_edge(6,5)
g.add_edge(7,5)
g.add_edge(8,7)
g.add_edge(10,9)
g.add_edge(11,9)
g.add_edge(12,11)


g.corret()

v1 = g.bfs(0)

g2 = Graph(13)

g2.add_edge(1,0)
g2.add_edge(4,0)
g2.add_edge(2,1)
g2.add_edge(3,1)
g2.add_edge(5,4)
g2.add_edge(9,4)
g2.add_edge(6,5)
g2.add_edge(7,5)
g2.add_edge(8,7)
g2.add_edge(10,9)
g2.add_edge(11,9)
g2.add_edge(12,11)

g2.corret()

v2 = g.bfs(v1)

print(v1,v2)