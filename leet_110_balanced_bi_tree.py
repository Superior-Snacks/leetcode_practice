# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
ég fæ bi tree, þarf að finna hvrot það er height ballanced það þýðri að hægri hliðin og vinstri eru jafn djúp,
fer ég bara í gegnum það frá vinstri til hægri og ef dýptin er komin lengra en fyrsta línan þá break-a me true?
"""
class Solution(object):
    def isBalanced(self, root):
        ...
        

sol = Solution
# Balanced tree
print("Test 1:", sol.isBalanced([3, 9, 20, None, None, 15, 7]), "Expected: True")

# Unbalanced tree
print("Test 2:", sol.isBalanced([1, 2, 2, 3, 3, None, None, 4, 4]), "Expected: False")

# Empty tree
print("Test 3:", sol.isBalanced([]), "Expected: True")

# Single node
print("Test 4:", sol.isBalanced([1]), "Expected: True")

# Slightly unbalanced (deeper on one side by 2 levels)
print("Test 5:", sol.isBalanced([1, 2, None, 3]), "Expected: False")

# Perfectly balanced
print("Test 6:", sol.isBalanced([1, 2, 3, 4, 5, 6, 7]), "Expected: True")
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