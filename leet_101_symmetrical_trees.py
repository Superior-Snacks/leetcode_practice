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

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

x = Solution()
sol = [1, 2, 2, 3, 4, 4, 3]
tree = build_tree(sol)
print("Test 1:", x.isSymmetric(tree))  # Expected: True

sol = [1, 2, 2, None, 3, None, 3]
tree = build_tree(sol)
print("Test 2:", x.isSymmetric(tree))  # Expected: False

sol = [1]
tree = build_tree(sol)
print("Test 3:", x.isSymmetric(tree))  # Expected: True

sol = []
tree = build_tree(sol)
print("Test 4:", x.isSymmetric(tree))  # Expected: True (if empty tree is considered symmetric)

sol = [1, 2, None]
tree = build_tree(sol)
print(tree.val)
print("Test 5:", x.isSymmetric(tree))  # Expected: False

sol = [1, 2, 2, 3, 4, 4, 3, 5, None, None, 5, 5, None, None, 5]
tree = build_tree(sol)
print("Test 6:", x.isSymmetric(tree))  # Expected: True

sol = [1, 2, 2, 3, None, None, 3]
tree = build_tree(sol)
print("Test 7:", x.isSymmetric(tree))  # Expected: False