#!/usr/bin/env python

from __typing__ import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    def dfs(root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(dfs(root.left), dfs(root.right))

    if not root:
        return 0
    else:
        return 1 + max(dfs(root.left), dfs(root.right))
