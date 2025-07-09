# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
def inorderTraversal(root):
    while True:
        ...


# Example 1
print("Case 1:", inorderTraversal([1, None, 2, 3]), "Expected: [1, 3, 2]")

# Example 2
print("Case 2:", inorderTraversal([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]), "Expected: [4, 2, 6, 5, 7, 1, 3, 9, 8]")

# Example 3: Empty tree
print("Case 3:", inorderTraversal([]), "Expected: []")

# Example 4: Single node
print("Case 4:", inorderTraversal([1]), "Expected: [1]")

# Additional edge cases
print("Case 5:", inorderTraversal([1, 2]), "Expected: [2, 1]")
print("Case 6:", inorderTraversal([1, None, 2]), "Expected: [1, 2]")
print("Case 7:", inorderTraversal([1, 2, None, 3]), "Expected: [3, 2, 1]")

"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]


Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]


Example 3:

Input: root = []

Output: []


Example 4:

Input: root = [1]

Output: [1]

 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
Follow up: Recursive solution is trivial, could you do it iteratively?
"""