


#idiot correct is just 
def inorderTraversal(self, root):
    if not root:
        return []
    return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)




"""from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def build_tree(self, arr):
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

    def _traverse(self, root):
        if not root:
            return []
        return self._traverse(root.left) + [root.val] + self._traverse(root.right)

    def inorderTraversal(self, arr):
        tree = self.build_tree(arr)
        return self._traverse(tree)"""

"""    count = 0
    order = []
    indx = len(root).bit_length() - 1
    length = len(root)
    print(f"length: {length}")
    print(f"depth: {indx}")
    #go down left to right reverse when done
    #For node at index i:
    #Left child index: 2 * i + 1
    #Right child index: 2 * i + 2
    while count < length:
        #depth
        for i in range(indx):
            #calck ammount in index
            for j in range(i * 2):
                try:
                    print(root[2 * i + 1])
                except:
                    continue
        count += 1
"""
# Output: [4, 2, 6, 5, 7, 1, 3, 9, 8]
# Example 3: Empty tree
#print("Case 3:", inorderTraversal([]), "Expected: []")

# Example 4: Single node
#print("Case 4:", inorderTraversal([1]), "Expected: [1]")

# Additional edge cases
#print("Case 5:", inorderTraversal([1, 2]), "Expected: [2, 1]")
#print("Case 6:", inorderTraversal([1, None, 2]), "Expected: [1, 2]")
#print("Case 7:", inorderTraversal([1, 2, None, 3]), "Expected: [3, 2, 1]")

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