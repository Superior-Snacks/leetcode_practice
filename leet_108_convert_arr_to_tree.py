from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) / 2 #height ballanced means both sides are equally deep (keep it whole)
        if (mid % 1) == 0 and mid > 2: #if the tree is even the leftmost indext is used (dose not aply to too small numbersets)
            mid = int(mid) - 1
        else:
            mid = int(mid)
        #now add to tree
        #can rearrange to fit, prolly not optimal, just go backwards for left side?
        tree = TreeNode(nums[mid])
        print(tree.val)
        root = nums[mid]
        left = nums[:mid]
        right = reversed(nums[mid+1:])
        print(root)
        print(left, right)

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