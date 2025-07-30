class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        mid = len(nums) / 2 #height ballanced means both sides are equally deep (keep it whole)
        if (mid % 1) == 0 and mid > 2: #if the tree is even the leftmost indext is used (dose not aply to too small numbersets)
            mid = int(mid) - 1
        else:
            mid = int(mid)
        #now add to tree

"""
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""
sol = Solution()
print(sol.sortedArrayToBST([-10,-3,0,5,9]))       # Mid is 0, expected root = 0
print(sol.sortedArrayToBST([-11,-8,0,1,10,20]))#? 0 or 1
print(sol.sortedArrayToBST([-11,-8,1,8,100]))     # mid is 1 expected root = 0
print(sol.sortedArrayToBST([1,3]))               # Small even-size input
print(sol.sortedArrayToBST([1]))                 # One element
print(sol.sortedArrayToBST([]))                  # Empty list (edge case)
print(sol.sortedArrayToBST([1,2,3,4,5,6,7]))      # Perfectly balanced possible
print(sol.sortedArrayToBST([-10000, 0, 10000]))   # Large number boundaries
print(sol.sortedArrayToBST(list(range(1, 10001))))# Very large input for stress test