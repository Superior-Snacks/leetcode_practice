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
    def postorderTraversal(self, root):
        result = []
        if not root:
            return result
        
        stack = [root]
        while stack:        # while something is in the stack
            node = stack.pop()       # take the top item out
            result.append(node.val)# add this node’s value to result

            if node.right:# if node has a right child:
                stack.append(node.right)# push right child onto stack

            if node.left:# if node has a left child:
                stack.append(node.left)# push left child onto stack
        flipp = result[0]
        return result[1:] + flipp
            

        


sol = Solution()
print(sol.postorderTraversal(build_tree([1,None,2,3])), "expected: [3,2,1]")
print(sol.postorderTraversal(build_tree([1,2,3,4,5,None,8,None,None,6,7,9])), "expected: [4,6,7,5,2,9,8,3,1]")
print(sol.postorderTraversal(build_tree([])), "expected: []")
print(sol.postorderTraversal(build_tree([1])), "expected: [1]")

"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,6,7,5,2,9,8,3,1]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]
 
Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

"""
works but not classy
class Solution(object):
    def postorderTraversal(self, root):
        if root == None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
"""