# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr):
    if not arr:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in arr]
    for i in range(len(arr)):
        if nodes[i] is not None:
            left = 2*i + 1
            right = 2*i + 2
            if left < len(arr): nodes[i].left = nodes[left]
            if right < len(arr): nodes[i].right = nodes[right]
    return nodes[0]

def inorderTraversal(root):
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

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
# Example 1
tree = build_tree([1, None, 2, 3])
print("Case 1:", inorderTraversal([1, None, 2, 3]), "Expected: [1, 3, 2]")

# Example 2
tree = build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
print("Case 2:", inorderTraversal([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]), "Expected: [4, 2, 6, 5, 7, 1, 3, 9, 8]")
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