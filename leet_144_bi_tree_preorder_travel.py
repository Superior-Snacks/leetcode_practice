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
    def preorderTraversal(self, root):
        result = []
        if not root:
            return result   # handle empty tree

        stack = []          # start with a stack
        stack.append(root)  # put the root in

        while stack:        # while something is in the stack
            node = stack.pop()       # take the top item out
            result.append(node.val)# add this node’s value to result

            # if node has a right child:
                # push right child onto stack

            # if node has a left child:
                # push left child onto stack

        return result
        



    

sol = Solution()
print(sol.preorderTraversal(build_tree([1,None,2,3])), "expected: [1,2,3]")
print(sol.preorderTraversal(build_tree([1,2,3,4,5,None,8,None,None,6,7,9])), "expected: [1,2,4,5,6,7,3,8,9]")
print(sol.preorderTraversal(build_tree([])), "expected: []")
print(sol.preorderTraversal(build_tree([1])), "expected: [1]")
print(sol.preorderTraversal(build_tree([1,2,None,3])), "expected: [1,2,3]")  # skewed left tree
print(sol.preorderTraversal(build_tree([1,None,2,None,3])), "expected: [1,2,3]")  # skewed right tree
"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]
Explanation:

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [1,2,4,5,6,7,3,8,9]
Explanation:

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

"""
works
class Solution(object):
    def preorderTraversal(self, root):
        if root == None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
"""