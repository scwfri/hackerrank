#!/usr/bin/env python

from typing import Optional

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return
    res = []
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
        res.append(this_level)
        q = next_level

    return res
