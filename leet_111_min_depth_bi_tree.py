from collections import deque
#Definition for a binary tree node.
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
    def minDepth(self, root):
        ...





sol = Solution
print(sol.minDepth(build_tree([3,9,20,None,None,15,7])), "expected:", 2)      # normal balanced tree
print(sol.minDepth(build_tree([2,None,3,None,4,None,5,None,6])), "expected:", 5) # skewed right
print(sol.minDepth(build_tree([])), "expected:", 0)                           # empty tree
print(sol.minDepth(build_tree([1])), "expected:", 1)                          # single node
print(sol.minDepth(build_tree([1,2])), "expected:", 2)                        # root + left child
print(sol.minDepth(build_tree([1,None,2])), "expected:", 2)                   # root + right child
print(sol.minDepth(build_tree([1,2,3,4,None,None,None])), "expected:", 3)     # only one leaf deep on one side
"""
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""