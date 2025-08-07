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
"""
ég fæ bi tree, þarf að finna hvrot það er height ballanced það þýðri að hægri hliðin og vinstri eru jafn djúp,
fer ég bara í gegnum það frá vinstri til hægri og ef dýptin er komin lengra en fyrsta línan þá break-a me true?

er það bara recursive left left þar til none svo right?
"""
class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        

sol = Solution()
# Balanced tree
print("Test 1:", sol.isBalanced(build_tree([3, 9, 20, None, None, 15, 7])), "Expected: True")

# Unbalanced tree
print("Test 2:", sol.isBalanced(build_tree([1, 2, 2, 3, 3, None, None, 4, 4])), "Expected: False")

# Empty tree
print("Test 3:", sol.isBalanced(build_tree([])), "Expected: True")

# Single node
print("Test 4:", sol.isBalanced(build_tree([1])), "Expected: True")

# Slightly unbalanced (deeper on one side by 2 levels)
print("Test 5:", sol.isBalanced(build_tree([1, 2, None, 3])), "Expected: False")

# Perfectly balanced
print("Test 6:", sol.isBalanced(build_tree([1, 2, 3, 4, 5, 6, 7])), "Expected: True")
"""
Given a binary tree, determine if it is height-balanced.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""