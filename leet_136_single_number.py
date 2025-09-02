class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
     

sol = Solution()

print(sol.singleNumber([2, 2, 1]), "expected:", 1)
print(sol.singleNumber([4, 1, 2, 1, 2]), "expected:", 4)
print(sol.singleNumber([1]), "expected:", 1)

# zeros
print(sol.singleNumber([0, 1, 0]), "expected:", 1)
print(sol.singleNumber([0]), "expected:", 0)

# negatives & mix
print(sol.singleNumber([-1, 2, -1]), "expected:", 2)
print(sol.singleNumber([-3, -3, -4]), "expected:", -4)
print(sol.singleNumber([-5, -1, -1, -2, -2]), "expected:", -5)

# single at boundaries
print(sol.singleNumber([9, 1, 1, 2, 2, 3, 3]), "expected:", 9)     # single at start
print(sol.singleNumber([5, 6, 6, 7, 7, 8, 8, 5, 10]), "expected:", 10)  # single at end

# variety / sanity
print(sol.singleNumber([10, 14, 10, 14, 13]), "expected:", 13)
print(sol.singleNumber([10000, -10000, 3, 3, 10000]), "expected:", -10000)
print(sol.singleNumber([2,2,3,3,4,4,5,5,6,6,7]), "expected:", 7)

# a few more
print(sol.singleNumber([11, 11, 12]), "expected:", 12)
print(sol.singleNumber([42, 0, 42]), "expected:", 0)
print(sol.singleNumber([-100, -100, 999]), "expected:", 999)
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""