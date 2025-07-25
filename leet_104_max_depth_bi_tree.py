from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        node = queue.popleft()
        if node:
            if i < len(arr):
                left_val = arr[i]
                node.left = TreeNode(left_val) if left_val is not None else None
                queue.append(node.left)
                i += 1
            if i < len(arr):
                right_val = arr[i]
                node.right = TreeNode(right_val) if right_val is not None else None
                queue.append(node.right)
                i += 1
    return root


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
        