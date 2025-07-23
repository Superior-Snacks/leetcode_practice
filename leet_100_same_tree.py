# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


        
def isSameTree(self, p, q):
    """
    :type p: Optional[TreeNode]
    :type q: Optional[TreeNode]
    :rtype: bool
    """


# Case 1: Same structure, same values
#    1       1
#   / \     / \
#  2   3   2   3
# => True
print("Test 1", isSameTree(tree1, tree2), "Expected: True")

# Case 2: One tree has missing left child
#    1       1
#   /         \
#  2           2
# => False
print("Test 2", isSameTree(tree3, tree4), "Expected: False")

# Case 3: Structure same, values different
#    1       1
#   / \     / \
#  2   1   1   2
# => False
print("Test 3", isSameTree(tree5, tree6), "Expected: False")

# Edge Case: Both trees empty
# => True
print("Test 4", isSameTree(None, None), "Expected: True")

# Edge Case: One empty, one not
# => False
print("Test 5", isSameTree(TreeNode(1), None), "Expected: False")