class Solution(object):
    def majorityElement(self, nums):
        count = 0
        curr = None
        for i in nums:
            if count == 0:
                curr = i
                count += 1
            else:
                if curr == i:
                    count += 1
                else:
                    count -= 1
        return curr




        
sol = Solution()
print(sol.majorityElement([3,2,3]), "expected: 3")
print(sol.majorityElement([2,2,1,1,1,2,2]), "expected: 2")
print(sol.majorityElement([1]), "expected: 1")
print(sol.majorityElement([1,1,2]), "expected: 1")
print(sol.majorityElement([6,5,5]), "expected: 5")
"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

"""
first attempt
class Solution(object):
    def majorityElement(self, nums):
        bar = len(nums) // 2
        collection = {}
        for i in nums:
            if i not in collection:
                collection[i] = 1
            else:
                collection[i] += 1
        if collection[i] > bar:
            return i
        return next(iter(collection))
"""