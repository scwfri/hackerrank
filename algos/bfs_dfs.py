#!/usr/bin/env python

from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: Node
    right: Node


""""
   3
  /  \
2      7
      /  \
     6   10
"""

n10 = Node(10, None, None)
n6 = Node(6, None, None)
n7 = Node(7, n6, n10)
n2 = Node(2, None, None)
n3 = Node(3, n2, n7)


def dfs(head: Node):
    if not head:
        return
    if head.left:
        dfs(head.left)
    if head.right:
        dfs(head.right)
    if head.value:
        print(head.value)


def bfs(head: Node):
    q = deque()
    q.append(head)
    while q:
        item = q.popleft()
        if item.left:
            q.append(item.left)
        if item.right:
            q.append(item.right)
        print(item.value)

        
def kth_smallest(head: Node, k: int) -> int:
    """Find kth smallest node in a binary tree
    """
    items = []
    node = head
    stack = [node]
    
    while node or stack:
        while node: 
            stack.append(node.left)
            node = node.left
        
        node = stack.pop()
        if node:
            items.append(node.value)
            node = node.right
        
    return items

print('DFS:')
dfs(n3)
print('BFS:')
bfs(n3)
