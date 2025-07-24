# Definition for a binary tree node.
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

def isSameTree(p, q):
    ...


# Case 1: Same structure, same values
#    1       1
#   / \     / \
#  2   3   2   3
# => True
tree1 = build_tree([1,2,3])
tree2 = build_tree([1,2,3])
print("Test 1", isSameTree(tree1, tree2), "Expected: True")
print(tree1.right.val)
# Case 2: One tree has missing left child
#    1       1
#   /         \
#  2           2
# => False
tree3 = build_tree([1,2])
tree4 = build_tree([1,None,2])
print("Test 2", isSameTree(tree3, tree4), "Expected: False")

# Case 3: Structure same, values different
#    1       1
#   / \     / \
#  2   1   1   2
# => False
tree5 = build_tree([1,2,1])
tree6 = build_tree([1,1,2])
print("Test 3", isSameTree(tree5, tree6), "Expected: False")

# Edge Case: Both trees empty
# => True
print("Test 4", isSameTree(None, None), "Expected: True")

# Edge Case: One empty, one not
# => False
print("Test 5", isSameTree(TreeNode(1), None), "Expected: False")