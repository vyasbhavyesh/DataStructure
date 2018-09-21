#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 05:24:36 2018

@author: babavyas
"""
arr = [10,8,7,5,3,16,1]


def build_heap(arr):
    for i in range(len(arr)//2,-1,-1):
        heapi(arr,i,len(arr))
    
    
def heap_sort(arr):
    print(arr[0])
    for i in range(len(arr)-1,0,-1):
        arr[i],arr[0] = arr[0], arr[i]
        heapi(arr,0,i)
    

def heapi(arr,n,le):
    print("le is",le)
    left_node = n * 2 + 1
    right_node = n * 2 + 2
    root_node = n
    lar = n
    if left_node < le and arr[left_node] < arr[root_node]:
        lar = left_node
    if right_node < le and arr[right_node] < arr[lar]:
        lar = right_node
    if arr[lar] != arr[n]:
        arr[n], arr[lar] = arr[lar], arr[n]
        heapi(arr,lar,le)
        