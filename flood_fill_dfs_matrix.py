#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 00:17:23 2018

@author: babavyas
Connected Cells in a
Grid
Consider a matrix where each cell contains either a or a . Any cell containing a is called a filled cell.
Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally.
In the following grid, all cells marked X are connected to the cell marked Y .
XXX
XYX
XXX
If one or more filled cells are also connected, they form a region. Note that each cell in a region is
connected to zero or more cells in the region but is not necessarily directly connected to all the other cells
in the region.
Task
Given an matrix, find and print the number of cells in the largest region in the matrix. Note that
there may be more than one region in the matrix.
Input Format
The first line contains an integer , the number of rows in the matrix.
The second line contains an integer , the number of columns in the matrix.
Each of the next lines contains space-separated integers matrix[i][j].
Constraints
Output Format
Print the number of cells in the largest region in the given matrix.
Sample Input
4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0
Sample Output
5
Explanation
The diagram below depicts two regions of the matrix; for each region, the component cells forming the
region are marked with an X:
X X 0 0     1 1 0 0
0 X X 0     0 1 1 0
0 0 X 0     0 0 1 0
1 0 0 0     X 0 0 0
The first region has five cells and the second region has one cell. We print the size of the largest region.

"""

#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the connectedCell function below.

def DFS(x, y, visited, n, m,matrix,c):
    if (x >= n or y >= m):
        return
    if(x < 0 or y < 0):
        return
    if(visited[x][y] == True or matrix[x][y] == 0):
        return
    visited[x][y] = True
    c.append(1)
    DFS(x-1, y-1, visited, n, m,matrix,c)
    DFS(x-1, y, visited, n, m,matrix,c)
    DFS(x-1, y+1, visited, n, m,matrix,c)
    DFS(x, y-1, visited, n, m,matrix,c)
    DFS(x, y+1, visited, n, m,matrix,c)
    DFS(x+1, y-1, visited, n, m,matrix,c)
    DFS(x+1, y, visited, n, m,matrix,c)
    DFS(x+1, y+1, visited, n, m,matrix,c)
    
    

def connectedCell(matrix):
    n = len(matrix)
    m = len(matrix[0])
    visited = []
    res = []
    for i in range(n):
        z = []
        for j in range(m):
            z.append(False)
        visited.append(z)
    #print(n,m)
    for i in range(n):
        for j in range(m):
            c = []
            if matrix[i][j] == 1 and visited[i][j] == False:
                DFS(i,j,visited,n,m,matrix,c)
                res.append(len(c))
    return max(res)
    
    
    DFS(0,0,visited,n,m,matrix,c)
    res = len(c)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()