#!/usr/bin/env python

from typing import Optional

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return
    res = collections.deque() # or just reverse a list at the end
    q = [root]
    while q:
        this_level = []
        next_level = []
        for node in q:
            this_level.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        res.appendleft(this_level)
        q = next_level
