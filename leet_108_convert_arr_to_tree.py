# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """


sol = Solution
print(sol.sortedArrayToBST([-10,-3,0,5,9]))       # Mid is 0, expected root = 0
print(sol.sortedArrayToBST([1,3]))               # Small even-size input
print(sol.sortedArrayToBST([1]))                 # One element
print(sol.sortedArrayToBST([]))                  # Empty list (edge case)
print(sol.sortedArrayToBST([1,2,3,4,5,6,7]))      # Perfectly balanced possible
print(sol.sortedArrayToBST([-10000, 0, 10000]))   # Large number boundaries
print(sol.sortedArrayToBST(list(range(1, 10001))))# Very large input for stress test