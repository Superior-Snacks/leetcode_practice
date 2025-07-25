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
sol = Solution()

# Test 1: Full tree
arr = [1, 2, 2, 3, 4, 4, 3]
tree = build_tree(arr)
print(tree.left.left.val)
print("Test 1:", sol.maxDepth(tree), "Expected: 3")

# Test 2: Empty tree
arr = []
tree = build_tree(arr)
print("Test 2:", sol.maxDepth(tree), "Expected: 0")

# Test 3: Single node
arr = [1]
tree = build_tree(arr)
print("Test 3:", sol.maxDepth(tree), "Expected: 1")

# Test 4: Unbalanced right-heavy tree
arr = [1, None, 2, None, 3]
tree = build_tree(arr)
print("Test 4:", sol.maxDepth(tree), "Expected: 3")

# Test 5: Left-leaning tree
arr = [1, 2, None, 3, None]
tree = build_tree(arr)
print("Test 5:", sol.maxDepth(tree), "Expected: 3")

# Test 6: Balanced binary tree
arr = [1, 2, 3, 4, 5, 6, 7]
tree = build_tree(arr)
print("Test 6:", sol.maxDepth(tree), "Expected: 3")