#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 19:39:30 2018

@author: babavyas

Tree Data Structure
    Binary Tree
    BST
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
        
class BinaryTree:
    def __init__(self,root):
        self.root = root
            
    def insert(self,value):
        q = []
        q.append(self.root)
        
        while q:
            n = q.pop(0)
            
            if n.left == None:
                n.left = Node(value)
                break
            else:
                q.append(n.left)
            
            
            if n.right == None:
                n.right = Node(value)
                break
            else:
                q.append(n.right)
            
    
    def bfs(self,root):
        if root is None:
            return
        q = []
        q.append(root)
        while (len(q))>0:
            print(q[0].value)
            n = q.pop(0)
            if n.left is not None:
                q.append(n.left)
            if n.right is not None:
                q.append(n.right)
                
    def inorder(self,root):
        if root is None:
            return
            
        self.inorder(root.left)
        print(root.value)
        self.inorder(root.right)
    
    def preorder(self,root):
        if root is None:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)
            
    def delete(self,root,value):
        pass
        
        
        
root = Node(1)
b = BinaryTree(root)
b.insert(2)
b.insert(3)
b.insert(4)
b.insert(5)
b.insert(6)
b.insert(7)
b.insert(8)
b.bfs(root)
print('/n-----')
b.preorder(root)