class Solution(object):
    def sortedArrayToBST(self, nums):
        print(nums)


sol = Solution()
print(sol.sortedArrayToBST([-10,-3,0,5,9]))       # Mid is 0, expected root = 0
print(sol.sortedArrayToBST([-11,-8,0,1,100]))
print(sol.sortedArrayToBST([-11,-8,1,8,100]))     # mid is 1 expected root = 0
print(sol.sortedArrayToBST([1,3]))               # Small even-size input
print(sol.sortedArrayToBST([1]))                 # One element
print(sol.sortedArrayToBST([]))                  # Empty list (edge case)
print(sol.sortedArrayToBST([1,2,3,4,5,6,7]))      # Perfectly balanced possible
print(sol.sortedArrayToBST([-10000, 0, 10000]))   # Large number boundaries
print(sol.sortedArrayToBST(list(range(1, 10001))))# Very large input for stress test