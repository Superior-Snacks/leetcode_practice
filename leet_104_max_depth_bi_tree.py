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
sol = Solution
# 1. Empty tree
print("Test 1:", sol.maxDepth(None), "Expected: 0")

# 2. Single node
print("Test 2:", sol.maxDepth(TreeNode(1)), "Expected: 1")

# 3. Two-level tree
#        1
#       /
#      2
print("Test 3:", sol.maxDepth(TreeNode(1, TreeNode(2))), "Expected: 2")

# 4. Unbalanced tree (right heavy)
#        1
#         \
#          2
#           \
#            3
print("Test 4:", sol.maxDepth(TreeNode(1, None, TreeNode(2, None, TreeNode(3)))), "Expected: 3")

# 5. Balanced tree
#        1
#       / \
#      2   3
#     / \
#    4   5
print("Test 5:", sol.maxDepth(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))), "Expected: 3")