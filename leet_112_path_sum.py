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
    def hasPathSum(self, root, targetSum):
        return self.path_check(root, targetSum) == targetSum
    
    def path_check(self, root, remain_before):
        if (root.left == None) and (root.right == None) and remain_before == 0:

        


"""
        if not root:
            return 0
        left_height = self.isBalancedcalc(root.left)
        if left_height == -1:
            return -1
        right_height = self.isBalancedcalc(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return max(left_height, right_height) + 1
"""

sol = Solution()
# basic examples from the prompt
print("T1", sol.hasPathSum(build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1]), 22), "expected:", True)
print("T2", sol.hasPathSum(build_tree([1,2,3]), 5), "expected:", False)
print("T3", sol.hasPathSum(build_tree([]), 0), "expected:", False)
# single-node trees
print("T4", sol.hasPathSum(build_tree([7]), 7), "expected:", True)    # single node equals target
print("T5", sol.hasPathSum(build_tree([7]), 8), "expected:", False)   # single node not equal
# internal node equals target but is NOT a leaf — should be False
print("T6", sol.hasPathSum(build_tree([5,5,None]), 5), "expected:", False)
# multiple leaves, only one matches
print("T7", sol.hasPathSum(build_tree([1,2,3,4,5]), 8), "expected:", True)  
print("T8_fix", sol.hasPathSum(build_tree([1,2,3,4,5]), 9), "expected:", False)
# zeros involved
print("T9", sol.hasPathSum(build_tree([0,0,0,0,None,None,0]), 0), "expected:", True)   
print("T10", sol.hasPathSum(build_tree([0,1,2]), 0), "expected:", False)               
# negative numbers
print("T11", sol.hasPathSum(build_tree([-2,None,-3]), -5), "expected:", True)  
print("T12", sol.hasPathSum(build_tree([1,-2,-3,1,3,-2,None,-1]), -1), "expected:", True)
# skewed trees (deep like a linked list)
print("T13", sol.hasPathSum(build_tree([1,2,None,3,None,4,None,5]), 15), "expected:", True)  
print("T14", sol.hasPathSum(build_tree([1,2,None,3,None,4,None,5]), 16), "expected:", False)
# multiple valid paths exist — any one makes it True
print("T15", sol.hasPathSum(build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1]), 18), "expected:", True) 
# target negative with mixed values
print("T16", sol.hasPathSum(build_tree([2,-1,-2,None,None,-3,1]), -3), "expected:", True)  
# large absolute values
print("T17_fix", sol.hasPathSum(build_tree([1000,None,0,None,0]), 1000), "expected:", True)  
# empty target on non-empty tree
print("T18", sol.hasPathSum(build_tree([1,0,0]), 0), "expected:", False)  
# balanced vs unbalanced shapes
print("T19", sol.hasPathSum(build_tree([3,9,20,None,None,15,7]), 30), "expected:", True)  
print("T20", sol.hasPathSum(build_tree([3,9,20,None,None,15,7]), 12), "expected:", True)  
"""
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""